from nameko.rpc import rpc, RpcProxy


class ServiceOne:
    name = "service_one"

    service_two = RpcProxy("service_two")

    @rpc
    def entrypoint(self):

        print(self.service_two.sum(1,1))
