import time

class Debouncer:
    def __init__(self, cooldown=1.0):
        self.last_event = {}
        self.cooldown = cooldown

    def allow(self, event_name):
        now = time.time()

        if event_name not in self.last_event:
            self.last_event[event_name] = now
            return True

        if now - self.last_event[event_name] > self.cooldown:
            self.last_event[event_name] = now
            return True

        return False