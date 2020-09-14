import cv2
import numpy as np
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("trained_models/shape_predictor_68_face_landmarks.dat")
frame = cv2.imread("raw_data/images/face1.jpg")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = detector(gray)
color = (0, 255, 0)
for face in faces:

    x1 = face.left()    
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    # cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)
    #Just making the box bigger so it fit better
    x1 -= int(x1/25)
    y1 -= int(y1/25)
    x2 += int(x2/25)
    y2 += int(y2/25)

    #Putting a box around the face 
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    landmarks = predictor(gray, face)

    #Marking the 68 face landmarks
    for i in range(0, 68):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        cv2.circle(frame, (x, y), 2, color, -1)            
    """
    The 68 face landmarks in details:
        Jawline            0:16
        Right eyebrow      17:21
        Left eyebrow       22:26
        Nose line          27:30
        Lower nose line    31:35
        Right eye          36:41
        Left eye           42:47
        Ouuter lips        48:59
        Inner lips         60:67
    """

cv2.imshow("frame", frame)
cv2.imwrite("raw_data/images/include_face1_after.jpg", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()