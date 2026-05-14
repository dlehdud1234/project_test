class PolicyEngine:

    def resolve(self, gesture):

        mapping = {
            "OPEN_PALM": "PLAY_PAUSE",

            "SWIPE_RIGHT": "NEXT_VIDEO",
            "SWIPE_LEFT": "PREV_VIDEO",

            "SWIPE_UP": "VOLUME_UP",
            "SWIPE_DOWN": "VOLUME_DOWN"
        }

        return mapping.get(gesture)