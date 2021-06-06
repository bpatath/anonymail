import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from .models import Recipient
from apps.alias.schema import AliasConnectionType

#------
# Types

class RecipientType(DjangoObjectType):
    class Meta:
        model = Recipient
        fields = ('id', 'name', 'address', 'aliases', 'owner', 'enabled')
        interfaces = (relay.Node, )

    aliases = relay.ConnectionField(AliasConnectionType)

class RecipientConnectionType(relay.Connection):
    class Meta:
        node = RecipientType

#----------
# Mutations

class CreateRecipient(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        enabled = graphene.Boolean()

    recipient = graphene.Field(RecipientType)

    @staticmethod
    def mutate_and_get_payload(root, info, name, address, enabled):
        pass
    
class UpdateRecipient(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String()
        address = graphene.String()
        enabled = graphene.Boolean()

    recipient = graphene.Field(RecipientType)

    @staticmethod
    def mutate_and_get_payload(root, info, id, name, address, enabled):
        pass

class DeleteRecipient(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate_and_get_payload(root, info, id):
        pass

class Mutation(graphene.ObjectType):
    createRecipient = graphene.Field(CreateRecipient)
    updateRecipient = graphene.Field(UpdateRecipient)
    deleteRecipient = graphene.Field(DeleteRecipient)
