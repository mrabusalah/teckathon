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
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 1)

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
    #region Landmarks in a nuttshel
    #Jawline 
    start_x = landmarks.part(0).x
    start_y = landmarks.part(0).y
    for point in range(1, 17):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
        
    #Right eyebrow
    start_x = landmarks.part(17).x
    start_y = landmarks.part(17).y
    for point in range(18, 22):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y

    #Left eyebrow
    start_x = landmarks.part(22).x
    start_y = landmarks.part(22).y
    for point in range(23, 27):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    
    #Nose line
    start_x = landmarks.part(27).x
    start_y = landmarks.part(27).y
    for point in range(28, 31):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    
    #Lower nose line
    start_x = landmarks.part(31).x
    start_y = landmarks.part(31).y
    for point in range(32, 36):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    
    #Right eye 
    start_x = landmarks.part(36).x
    start_y = landmarks.part(36).y
    for point in range(37, 42):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    cv2.line(frame, (start_x, start_y), (landmarks.part(36).x, landmarks.part(36).y), color, 1)

    #Left eye
    start_x = landmarks.part(42).x
    start_y = landmarks.part(42).y
    for point in range(43, 48):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    cv2.line(frame, (start_x, start_y), (landmarks.part(42).x, landmarks.part(42).y), color, 1)

    #Outter lips
    start_x = landmarks.part(48).x
    start_y = landmarks.part(48).y
    for point in range(49, 60):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    cv2.line(frame, (start_x, start_y), (landmarks.part(48).x, landmarks.part(48).y), color, 1)            

    #Inner lips
    start_x = landmarks.part(60).x
    start_y = landmarks.part(60).y
    for point in range(61, 68):
        end_x = landmarks   .part(point).x
        end_y = landmarks.part(point).y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    cv2.line(frame, (start_x, start_y), (landmarks.part(60).x, landmarks.part(60).y), color, 1)            

    #Connecting the jaw line with the eyebrows 
    jawline_startpoints = (landmarks.part(0).x, landmarks.part(0).y)
    jawline_endpoints = (landmarks.part(16).x, landmarks.part(16).y)

    left_eyebrow_startpoints = (landmarks.part(17).x, landmarks.part(17).y)

    cv2.line(frame, jawline_startpoints, left_eyebrow_startpoints, color, 1)
    right_eyebrow_startpoints = (landmarks.part(26).x, landmarks.part(26).y)
    cv2.line(frame, jawline_endpoints, right_eyebrow_startpoints, color, 1)
    #endregion
cv2.imshow("frame", frame)
cv2.imwrite("raw_data/images/include_face1_after.jpg", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()