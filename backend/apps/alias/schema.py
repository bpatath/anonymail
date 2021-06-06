import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from .models import Alias
from apps.recipient.schema import RecipientConnectionType

#------
# Types

class AliasType(DjangoObjectType):
    class Meta:
        model = Alias
        fields = ('id', 'name', 'localpart', 'domain', 'isLocalpartRandom', 'owner', 'enabled')
        interfaces = (relay.Node, )

    recipients = relay.ConnectionField(RecipientConnectionType)

class AliasConnectionType(relay.Connection):
    class Meta:
        node = AliasType

#----------
# Mutations

class CreateAlias(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        localpart = graphene.String()
        domainId = graphene.ID(required=True)
        enabled = graphene.Boolean(required=True)

    alias = graphene.Field(AliasType)

    @staticmethod
    def mutate_and_get_payload(root, info, name, address, enabled):
        pass

class UpdateAlias(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String()
        enabled = graphene.Boolean()

    alias = graphene.Field(AliasType)

    @staticmethod
    def mutate_and_get_payload(root, info, id, name, enabled):
        pass

class DeleteAlias(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate_and_get_payload(root, info, id):
        pass

class Mutation(graphene.ObjectType):
    createAlias = graphene.Field(CreateAlias)
    updateAlias = graphene.Field(UpdateAlias)
    deleteAlias = graphene.Field(DeleteAlias)
