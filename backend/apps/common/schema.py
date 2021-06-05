import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from . import models

class User(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ('id', 'domains', 'aliases')
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    viewer = graphene.Field(User)

    def resolve_viewer(root, info):
        if not info.context.user.is_authenticated:
            return None
        else:
            return info.context.user