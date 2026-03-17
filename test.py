import cv2
import mediapipe as mp
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

canvas = None
xp, yp = 0, 0

draw_color = (0,255,0)
brush_thickness = 5
eraser_size = 60

tipIds = [4,8,12,16,20]

pTime = 0

# Gesture stabilization
gesture_delay = 0.5
last_gesture_time = 0


def fingers_up(lmList, hand_type):

    fingers = []

    # Thumb detection (left/right fix)
    if hand_type == "Right":
        fingers.append(1 if lmList[4][0] < lmList[3][0] else 0)
    else:
        fingers.append(1 if lmList[4][0] > lmList[3][0] else 0)

    # Other fingers
    for id in range(1,5):
        fingers.append(1 if lmList[tipIds[id]][1] < lmList[tipIds[id]-2][1] else 0)

    return fingers


while True:

    success, frame = cap.read()
    frame = cv2.flip(frame,1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    h,w,_ = frame.shape

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    mode = "DRAW"

    if draw_color == (255,0,0):
        color_name = "BLUE"
    elif draw_color == (0,0,255):
        color_name = "RED"
    elif draw_color == (0,255,0):
        color_name = "GREEN"
    else:
        color_name = "ERASER"


    if results.multi_hand_landmarks:

        for handLms, handType in zip(results.multi_hand_landmarks, results.multi_handedness):

            hand_label = handType.classification[0].label

            lmList = []

            for id,lm in enumerate(handLms.landmark):
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append((cx,cy))

            mp_draw.draw_landmarks(frame,handLms,mp_hands.HAND_CONNECTIONS)

            fingers = fingers_up(lmList, hand_label)

            x_index,y_index = lmList[8]
            x_thumb,y_thumb = lmList[4]

            dist = math.hypot(x_index-x_thumb,y_index-y_thumb)

            current_time = time.time()

            # STOP (pinch)
            if dist < 40:

                mode = "STOP"
                xp, yp = 0,0


            # PALM ERASER
            elif fingers == [1,1,1,1,1]:

                mode = "ERASE"

                px,py = lmList[9]

                cv2.circle(canvas,(px,py),eraser_size,(0,0,0),-1)

                xp, yp = 0,0


            # BLUE
            elif fingers == [0,1,1,0,0]:

                if current_time - last_gesture_time > gesture_delay:
                    draw_color = (255,0,0)
                    last_gesture_time = current_time


            # RED
            elif fingers == [0,1,1,1,0]:

                if current_time - last_gesture_time > gesture_delay:
                    draw_color = (0,0,255)
                    last_gesture_time = current_time


            # GREEN
            elif fingers == [0,1,1,1,1]:

                if current_time - last_gesture_time > gesture_delay:
                    draw_color = (0,255,0)
                    last_gesture_time = current_time


            # CLEAR CANVAS (Closed Fist)
            elif fingers == [0,0,0,0,0]:

                if current_time - last_gesture_time > gesture_delay:
                    canvas = np.zeros_like(frame)
                    last_gesture_time = current_time
                    mode = "CLEAR"

                xp, yp = 0,0


            # DRAW
            elif fingers == [0,1,0,0,0]:

                mode = "DRAW"

                thickness = eraser_size if draw_color==(0,0,0) else brush_thickness

                if xp==0 and yp==0:
                    xp,yp = x_index,y_index

                # Smooth drawing
                x_smooth = int(xp + (x_index - xp) * 0.5)
                y_smooth = int(yp + (y_index - yp) * 0.5)

                cv2.circle(frame,(x_smooth,y_smooth),8,draw_color,-1)

                cv2.line(frame,(xp,yp),(x_smooth,y_smooth),draw_color,thickness)
                cv2.line(canvas,(xp,yp),(x_smooth,y_smooth),draw_color,thickness)

                xp,yp = x_smooth,y_smooth

            else:
                xp,yp = 0,0


    # Merge canvas with frame
    gray = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)
    _,inv = cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv,cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame,inv)
    frame = cv2.bitwise_or(frame,canvas)


    # FPS calculation
    cTime = time.time()
    fps = int(1/(cTime-pTime)) if (cTime-pTime)!=0 else 0
    pTime = cTime


    # UI BAR
    cv2.rectangle(frame,(0,0),(w,40),(40,40,40),-1)

    ui_text = f"MODE: {mode} | COLOR: {color_name} | BRUSH: {brush_thickness} | ERASER: {eraser_size} | FPS: {fps}"

    cv2.putText(frame,ui_text,(10,28),
                cv2.FONT_HERSHEY_SIMPLEX,0.65,(255,255,255),2)

    cv2.imshow("AIR DRAW",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()