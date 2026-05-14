import pyautogui

class KeyboardController:

    def play_pause(self):
        pyautogui.press("space")

    def volume_up(self):
        pyautogui.press("up")

    def volume_down(self):
        pyautogui.press("down")