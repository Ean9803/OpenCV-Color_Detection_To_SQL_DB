import cv2
import numpy as np

class VisionTracker:

    def __init__(self):
        self.upper = np.array([172,50,255], dtype=np.uint8)
        self.lower = np.array([0,0,168], dtype=np.uint8)

        self.video = cv2.VideoCapture(0)

    def ProcessVideo(self):
        ReturnCont = []

        self.success, self.img = self.video.read()
        self.image = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.mask = cv2.inRange(self.image, self.lower, self.upper)
        result = cv2.bitwise_and(self.img, self.img, mask=self.mask)
        self.contours, self.hierarchy = cv2.findContours(self.mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(self.contours) != 0:
            i = 0
            for contour in self.contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    printText = "Object[{Index:d}] ({XPOS:.2f}, {YPOS:.2f})"
                    cx = int(x + (w / 2))
                    cy = int(y + (h / 2))
                    ReturnCont.append([cx, cy])
                    cv2.circle(self.img, (cx, cy), 10, (0, 0, 255), 3)
                    cv2.putText(self.img, printText.format(Index=i, XPOS=x, YPOS=y), (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
                    i = i + 1
        cv2.imshow("Cam", self.img)
        return ReturnCont

    def CancelBtn(self):
        return cv2.waitKey(1) == 27

    def FinishVideo(self):
        self.video.release()
        cv2.destroyAllWindows()

"""
Vis = VisionTracker()

while not Vis.CancelBtn():
    Vis.ProcessVideo()
Vis.FinishVideo()
"""