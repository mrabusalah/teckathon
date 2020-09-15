import cv2
import numpy as np
import dlib
import csv
import sys


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("trained_models/shape_predictor_68_face_landmarks.dat")
frame = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = detector(gray)
color = (0, 255, 0)
keys = list("face_left,face_top,face_right,face_bottom,jawline_0_x,jawline_0_y,jawline_1_x,jawline_1_y,jawline_2_x,jawline_2_y,jawline_3_x,jawline_3_y,jawline_4_x,jawline_4_y,jawline_5_x,jawline_5_y,jawline_6_x,jawline_6_y,jawline_7_x,jawline_7_y,jawline_8_x,jawline_8_y,jawline_9_x,jawline_9_y,jawline_10_x,jawline_10_y,jawline_11_x,jawline_11_y,jawline_12_x,jawline_12_y,jawline_13_x,jawline_13_y,jawline_14_x,jawline_14_y,jawline_15_x,jawline_15_y,jawline_16_x,jawline_16_y,right_eyebrow_17_x,right_eyebrow_17_y,right_eyebrow_18_x,right_eyebrow_18_y,right_eyebrow_19_x,right_eyebrow_19_y,right_eyebrow_20_x,right_eyebrow_20_y,right_eyebrow_21_x,right_eyebrow_21_y,left_eyebrow_17_x,left_eyebrow_17_y,left_eyebrow_23_x,left_eyebrow_23_y,left_eyebrow_24_x,left_eyebrow_24_y,left_eyebrow_25_x,left_eyebrow_25_y,left_eyebrow_26_x,left_eyebrow_26_y,nose_line_27_x,nose_line_27_y,nose_line_28_x,nose_line_28_y,nose_line_29_x,nose_line_29_y,nose_line_30_x,nose_line_30_y,lower_nose_line_31_x,lower_nose_line_31_y,lower_nose_line_32_x,lower_nose_line_32_y,lower_nose_line_33_x,lower_nose_line_33_y,lower_nose_line_34_x,lower_nose_line_34_y,lower_nose_line_35_x,lower_nose_line_35_y,right_eye_36_x,right_eye_36_y,right_eye_37_x,right_eye_37_y,right_eye_38_x,right_eye_38_y,right_eye_39_x,right_eye_39_y,right_eye_40_x,right_eye_40_y,right_eye_41_x,right_eye_41_y,left_eye_42_x,left_eye_42_y,left_eye_43_x,left_eye_43_y,left_eye_44_x,left_eye_44_y,left_eye_45_x,left_eye_45_y,left_eye_46_x,left_eye_46_y,left_eye_47_x,left_eye_47_y,outter_lips_48_x,outter_lips_48_y,outter_lips_49_x,outter_lips_49_y,outter_lips_50_x,outter_lips_50_y,outter_lips_51_x,outter_lips_51_y,outter_lips_52_x,outter_lips_52_y,outter_lips_53_x,outter_lips_53_y,outter_lips_54_x,outter_lips_54_y,outter_lips_55_x,outter_lips_55_y,outter_lips_56_x,outter_lips_56_y,outter_lips_57_x,outter_lips_57_y,outter_lips_58_x,outter_lips_58_y,outter_lips_59_x,outter_lips_59_y,inner_lips_60_x,inner_lips_60_y,inner_lips_61_x,inner_lips_61_y,inner_lips_62_x,inner_lips_62_y,inner_lips_63_x,inner_lips_63_y,inner_lips_64_x,inner_lips_64_y,inner_lips_65_x,inner_lips_65_y,inner_lips_66_x,inner_lips_66_y,inner_lips_67_x,inner_lips_67_y,focus".split(","))    
data = {}

face_detected = False

for face in faces:
    face_detected = True
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

    data['face_left'] = x1
    data['face_top'] = y1
    data['face_right'] = x2
    data['face_bottom'] = y2
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
    data['jawline_0_x'] = start_x
    data['jawline_0_y'] = start_y
    for point in range(1, 17):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        data[f'jawline_{point}_x'] = start_x
        data[f'jawline_{point}_y'] = start_y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
        
    #Right eyebrow
    start_x = landmarks.part(17).x
    start_y = landmarks.part(17).y
    data['right_eyebrow_17_x'] = start_x
    data['right_eyebrow_17_y'] = start_y
    for point in range(18, 22):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        data[f'right_eyebrow_{point}_x'] = start_x
        data[f'right_eyebrow_{point}_y'] = start_y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y

    #Left eyebrow
    start_x = landmarks.part(22).x
    start_y = landmarks.part(22).y
    data['left_eyebrow_17_x'] = start_x
    data['left_eyebrow_17_y'] = start_y
    for point in range(23, 27):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        data[f'left_eyebrow_{point}_x'] = start_x
        data[f'left_eyebrow_{point}_y'] = start_y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    
    #Nose line
    start_x = landmarks.part(27).x
    start_y = landmarks.part(27).y
    data['nose_line_27_x'] = start_x
    data['nose_line_27_y'] = start_y
    for point in range(28, 31):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        data[f'nose_line_{point}_x'] = start_x
        data[f'nose_line_{point}_y'] = start_y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    
    #Lower nose line
    start_x = landmarks.part(31).x
    start_y = landmarks.part(31).y
    data['lower_nose_line_31_x'] = start_x
    data['lower_nose_line_31_y'] = start_y
    for point in range(32, 36):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        data[f'lower_nose_line_{point}_x'] = start_x
        data[f'lower_nose_line_{point}_y'] = start_y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    
    #Right eye 
    start_x = landmarks.part(36).x
    start_y = landmarks.part(36).y
    data['right_eye_36_x'] = start_x
    data['right_eye_36_y'] = start_y
    for point in range(37, 42):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        data[f'right_eye_{point}_x'] = start_x
        data[f'right_eye_{point}_y'] = start_y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    cv2.line(frame, (start_x, start_y), (landmarks.part(36).x, landmarks.part(36).y), color, 1)

    #Left eye
    start_x = landmarks.part(42).x
    start_y = landmarks.part(42).y
    data['left_eye_42_x'] = start_x
    data['left_eye_42_y'] = start_y
    for point in range(43, 48):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        data[f'left_eye_{point}_x'] = start_x
        data[f'left_eye_{point}_y'] = start_y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    cv2.line(frame, (start_x, start_y), (landmarks.part(42).x, landmarks.part(42).y), color, 1)

    #Outter lips
    start_x = landmarks.part(48).x
    start_y = landmarks.part(48).y
    data['outter_lips_48_x'] = start_x
    data['outter_lips_48_y'] = start_y
    for point in range(49, 60):
        end_x = landmarks.part(point).x
        end_y = landmarks.part(point).y
        data[f'outter_lips_{point}_x'] = start_x
        data[f'outter_lips_{point}_y'] = start_y
        cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 1)
        start_x = end_x
        start_y = end_y
    cv2.line(frame, (start_x, start_y), (landmarks.part(48).x, landmarks.part(48).y), color, 1)            

    #Inner lips
    start_x = landmarks.part(60).x
    start_y = landmarks.part(60).y
    data['inner_lips_60_x'] = start_x
    data['inner_lips_60_y'] = start_y
    for point in range(61, 68):
        end_x = landmarks   .part(point).x
        end_y = landmarks.part(point).y
        data[f'inner_lips_{point}_x'] = start_x
        data[f'inner_lips_{point}_y'] = start_y
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
    focus = int(sys.argv[2])
    data['focus'] = focus
    #Break to get only the first face and not multiple faces
    break

#if a face is not detected then fill the data with zeros
if face_detected and focus == 1:
    with open( "csv/data.csv", 'a', newline='') as output_file:
        thewriter = csv.DictWriter(output_file, fieldnames=keys, quoting=csv.QUOTE_NONE, escapechar=' ')
        thewriter.writerow(data)
elif focus == 0:
    for key in keys:
        data[key] = 0
    data['focus'] = 0
    with open( "csv/data.csv", 'a', newline='') as output_file:
        thewriter = csv.DictWriter(output_file, fieldnames=keys, quoting=csv.QUOTE_NONE, escapechar=' ')
        thewriter.writerow(data)

cv2.imshow("frame", frame)
cv2.waitKey(1000)
cv2.destroyAllWindows()