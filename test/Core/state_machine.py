class AppState:
    PLAYING = "PLAYING"
    PAUSED = "PAUSED"

class StateMachine:
    def __init__(self):
        self.state = AppState.PAUSED

    def transition(self, event):
        if event == "PLAY_PAUSE":
            if self.state == AppState.PAUSED:
                self.state = AppState.PLAYING
            else:
                self.state = AppState.PAUSED