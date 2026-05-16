import cv2
import numpy as np
import matplotlib.pyplot as plt

absolute_truth = "Raghav Sucks!"
vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    height, width, _ = frame.shape
    frame = cv2.putText(frame, absolute_truth, (width - 250, height - 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA, False)
    frame = cv2.rectangle(frame, (width-270, height-75), (width, height), (0, 255, 0), 2)
    cv2.imshow(absolute_truth, frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
