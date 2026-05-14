class PolicyEngine:
    def resolve(self, gesture):
        mapping = {
            "OPEN_PALM": "PLAY_PAUSE",
            "SWIPE_RIGHT": "NEXT",
            "SWIPE_LEFT": "PREV"
        }

        return mapping.get(gesture)