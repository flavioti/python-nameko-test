import sys
from datetime import datetime

from nameko.events import EventDispatcher, event_handler
from nameko.timer import timer


class Service:
    name = "service"

    dispatch = EventDispatcher()

    @timer(interval=0.1)
    def ping(self):
        dt = datetime.now(tz=None)
        payload = {"datetime": dt}
        self.dispatch("evento_temporizado", payload)
        print(payload)
