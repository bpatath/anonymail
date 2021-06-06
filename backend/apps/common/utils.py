from graphene import relay

# This error is raised when the user gives a global id which does not
# correspond to the excepted node type
class InvalidNodeType(Error):
    pass

def get_pk_excpecting_type(id, type):
    id_type, pk = relay.from_global_id(id)
    if (id_type != type):
        raise InvalidNodeType()
    return pk



def parse_errors(e):
   pass 

class ErrorMutation(relay.ClientIDMutation):
    errors = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, *args, **kwargs):
        try:
            return cls.mutate(*args, **kwargs)
        except e:
            return cls(errors=parseErrors(e))

    def mutate(*args, **kwargs):
        raise NotImplementedError
