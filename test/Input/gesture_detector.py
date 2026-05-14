import time

class GestureDetector:
    def __init__(self):
        self.prev_wrist = None
        self.threshold = 0.08

        self.last_swipe_time = 0
        self.swipe_cooldown = 0.8  # 핵심

    def detect_swipe(self, lm):
        wrist = lm[0]

        if self.prev_wrist is None:
            self.prev_wrist = wrist
            return None

        dx = wrist.x - self.prev_wrist.x
        dy = wrist.y - self.prev_wrist.y

        self.prev_wrist = wrist

        now = time.time()

        # cooldown 체크 (중요)
        if now - self.last_swipe_time < self.swipe_cooldown:
            return None

        # 좌우 swipe
        if abs(dx) > abs(dy) and abs(dx) > self.threshold:

            self.last_swipe_time = now

            if dx > 0:
                return "SWIPE_RIGHT"
            else:
                return "SWIPE_LEFT"

        # 상하 swipe
        if abs(dy) > self.threshold:

            self.last_swipe_time = now

            if dy < 0:
                return "SWIPE_UP"
            else:
                return "SWIPE_DOWN"

        return None