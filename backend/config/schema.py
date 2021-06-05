import graphene
from apps.common import schema as CommonSchema
from apps.domain import schema as DomainSchema
from apps.alias import schema as AliasSchema

class Query(CommonSchema.Query, graphene.ObjectType):
    pass

class Mutation(DomainSchema.Mutation, AliasSchema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)