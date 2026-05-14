class ContextManager:
    def __init__(self):
        self.current_device = "laptop"
        self.mode = "youtube"  # youtube / idle

        self.state = "PAUSED"

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode