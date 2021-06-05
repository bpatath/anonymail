import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from . import models

class Alias(DjangoObjectType):
    class Meta:
        model = models.Alias
        fields = ('id', 'name', 'localpart', 'domain', 'owner', 'enabled')
        interfaces = (relay.Node, )

class CreateAlias(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        enabled = graphene.Boolean()