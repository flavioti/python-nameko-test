import sys
from datetime import datetime

from nameko.events import EventDispatcher, event_handler
from nameko.timer import timer


class Service:
    name = "service"

    @event_handler("service", "evento_temporizado")
    def ouvir(self, payload):
        print(payload)
