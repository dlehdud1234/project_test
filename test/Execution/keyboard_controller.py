import pyautogui

class KeyboardController:

    def play_pause(self):
        pyautogui.press("space")

    def next_video(self):
        pyautogui.hotkey("shift", "n")

    def prev_video(self):
        pyautogui.hotkey("shift", "p")

    def volume_up(self):
        pyautogui.press("up")

    def volume_down(self):
        pyautogui.press("down")