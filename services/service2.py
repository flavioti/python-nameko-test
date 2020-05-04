from nameko.rpc import rpc


class ServiceTwo:
    name = "service_two"

    @rpc
    def sum(self, num1, num2):
        print("B")
        return num1 + num2
