import time

class Logger:
    def log(self, tag, message):
        print(f"[{time.strftime('%H:%M:%S')}] [{tag}] {message}")