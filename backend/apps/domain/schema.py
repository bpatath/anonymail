import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from . import models

class Domain(DjangoObjectType):
    class Meta:
        model = models.Domain
        fields = ('id', 'name', 'address', 'owner', 'enabled')
        interfaces = (relay.Node, )

class CreateDomain(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        enabled = graphene.Boolean()

    domain = graphene.Field(Domain)

    @staticmethod
    def mutate_and_get_payload(root, info, name, address, enabled):
        domain = Domain(
            name=name,
            address=address,
            enabled=(enabled if enabled != None else True),
            owner=info.context.user
        )
        domain.save()
        return CreateDomain(domain=domain)

class UpdateDomain(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String()
        address = graphene.String()
        enabled = graphene.Boolean()

    domain = graphene.Field(Domain)

    @staticmethod
    def mutate_and_get_payload(root, info, id, name, address, enabled):
        domain = Domain.objects.get(pk=relay.from_global_id(id)[1])
        if name:    domain.name    = name
        if address: domain.address = address
        if enabled: domain.enabled = enabled
        domain.save()
        return UpdateDomain(domain=domain)

class DeleteDomain(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate_and_get_payload(root, info, id):
        domain = Domain.objects.get(pk=relay.from_global_id(id)[1])
        domain.delete()
        return DeleteDomain(ok=True)

class Mutation(graphene.ObjectType):
    createDomain = graphene.Field(CreateDomain)
    updateDomain = graphene.Field(UpdateDomain)
    deleteDomain = graphene.Field(DeleteDomain)