from Input.camera import CameraStream
from Input.gesture_detector import GestureDetector

from Events.event_bus import publish, consume
from Events.debounce import Debouncer

from Core.policy_engine import PolicyEngine
from Execution.youtube_controller import YouTubeController

camera = CameraStream()
detector = GestureDetector()

debouncer = Debouncer()

policy = PolicyEngine()
youtube = YouTubeController()

while True:
    frame = camera.read()

    gesture = detector.detect(frame)

    if gesture and debouncer.allow(gesture):

        action = policy.resolve(gesture)

        if action:
            youtube.execute(action)