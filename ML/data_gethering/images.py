import cv2
import numpy as np

frame = cv2.imread("raw_data/images/face1.jpg")
cv2.imshow("frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()