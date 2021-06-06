import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from .models import Domain

#------
# Types

class DomainType(DjangoObjectType):
    class Meta:
        model = Domain
        fields = ('id', 'name', 'address', 'owner', 'enabled')
        interfaces = (relay.Node, )

class DomainConnectionType(relay.Connection):
    class Meta:
        node = DomainType

#----------
# Mutations

class CreateDomain(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        allowChoosingLocalpart = graphene.Boolean(required=True)
        enabled = graphene.Boolean(required=True)

    domain = graphene.Field(DomainType)

    @staticmethod
    def mutate_and_get_payload(root, info, name, address, allowChoosingLocalpart, enabled):
        pass

class UpdateDomain(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String()
        address = graphene.String()
        allowChoosingLocalpart = graphene.Boolean()
        enabled = graphene.Boolean()

    domain = graphene.Field(DomainType)

    @staticmethod
    def mutate_and_get_payload(root, info, id, name, address, allowChoosingLocalpart, enabled):
        pass

class DeleteDomain(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate_and_get_payload(root, info, id):
        pass

class Mutation(graphene.ObjectType):
    createDomain = graphene.Field(CreateDomain)
    updateDomain = graphene.Field(UpdateDomain)
    deleteDomain = graphene.Field(DeleteDomain)
