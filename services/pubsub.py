from nameko.events import EventDispatcher, event_handler
from nameko.rpc import rpc


class ServiceA:
    name = "service_a"


    dispatch = EventDispatcher()

    @rpc
    def dispatching_method(self, payload):
        a = self.dispatch("event_type", payload)
        print(a)

class ServiceB:
    name = "service_b"

    @event_handler("service_a", "event_type")
    def handle_event(self, payload):
        print("service b received:", payload)