import cv2

class CameraStream:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def read(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def release(self):
        self.cap.release()