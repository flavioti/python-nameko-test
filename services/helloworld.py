from nameko.rpc import rpc, RpcProxy
from nameko.containers import ServiceContainer


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
