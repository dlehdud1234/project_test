from execution.keyboard_controller import KeyboardController

class YouTubeController:
    def __init__(self):
        self.keyboard = KeyboardController()

    def execute(self, action):
        if action == "PLAY_PAUSE":
            self.keyboard.play_pause()

        elif action == "VOLUME_UP":
            self.keyboard.volume_up()