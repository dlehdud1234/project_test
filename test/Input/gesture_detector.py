import mediapipe as mp

class GestureDetector:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands()

    def detect(self, frame):
        results = self.hands.process(frame)

        if results.multi_hand_landmarks:
            return "OPEN_PALM"

        return None