from graphene import ObjectType, String, Schema


class Query(ObjectType):

    # This defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # Our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return "Hello {}!".format(name)

    def resolve_goodbye(root, info):
        return "See ya!"


schema = Schema(query=Query)
