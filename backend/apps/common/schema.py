import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from apps.domain.schema import DomainConnectionType
from apps.recipient.schema import RecipientConnectionType
from apps.alias.scema import AliasConnectionType

class User(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ('id', 'domains', 'recipients', 'aliases')
        interfaces = (relay.Node, )

    domains = relay.ConnectionField(DomainConnectionType)
    recipients = relay.ConnectionField(RecipientConnectionType)
    aliases = relay.ConnectionField(AliasConnectionType)

class Query(graphene.ObjectType):
    viewer = graphene.Field(User)

    def resolve_viewer(root, info):
        if not info.context.user.is_authenticated:
            return None
        else:
            return info.context.user
