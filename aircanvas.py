import cv2
import numpy as np
import mediapipe as mp
from collections import deque

blue_points = [deque(maxlen=1024)]
green_points = [deque(maxlen=1024)]
red_points = [deque(maxlen=1024)]
yellow_points = [deque(maxlen=1024)]

blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

kernel = np.ones((5,5),np.uint8)

colorslist = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0


whitecanvas = np.zeros((471,636,3)) + 255
whitecanvas = cv2.rectangle(whitecanvas, (40,1), (140,65), (0,0,0), 2)
whitecanvas = cv2.rectangle(whitecanvas, (160,1), (255,65), (255,0,0), 2)
whitecanvas = cv2.rectangle(whitecanvas, (275,1), (370,65), (0,255,0), 2)
whitecanvas = cv2.rectangle(whitecanvas, (390,1), (485,65), (0,0,255), 2)
whitecanvas = cv2.rectangle(whitecanvas, (505,1), (600,65), (0,255,255), 2)

cv2.putText(whitecanvas, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(whitecanvas, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(whitecanvas, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(whitecanvas, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(whitecanvas, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)


mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)
ret = True
while ret:
    ret, userwindow = cap.read()

    x, y, c = userwindow.shape

    userwindow = cv2.flip(userwindow, 1)
    #hsv = cv2.cvtColor(userwindow, cv2.COLOR_BGR2HSV)
    userwindowrgb = cv2.cvtColor(userwindow, cv2.COLOR_BGR2RGB)

    userwindow = cv2.rectangle(userwindow, (40,1), (140,65), (0,0,0), 2)
    userwindow = cv2.rectangle(userwindow, (160,1), (255,65), (255,0,0), 2)
    userwindow = cv2.rectangle(userwindow, (275,1), (370,65), (0,255,0), 2)
    userwindow = cv2.rectangle(userwindow, (390,1), (485,65), (0,0,255), 2)
    userwindow = cv2.rectangle(userwindow, (505,1), (600,65), (0,255,255), 2)
    cv2.putText(userwindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(userwindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(userwindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(userwindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(userwindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    #userwindow = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    result = hands.process(userwindowrgb)

    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # # print(id, lm)
                # print(lm.x)
                # print(lm.y)
                lmx = int(lm.x * 640)
                lmy = int(lm.y * 480)

                landmarks.append([lmx, lmy])

            mpDraw.draw_landmarks(userwindow, handslms, mpHands.HAND_CONNECTIONS)
        fore_finger = (landmarks[8][0],landmarks[8][1])
        center = fore_finger
        thumb = (landmarks[4][0],landmarks[4][1])
        cv2.circle(userwindow, center, 3, (0,255,0),-1)
        print(center[1]-thumb[1])
        if (thumb[1]-center[1]<30):
            blue_points.append(deque(maxlen=512))
            blue_index += 1
            green_points.append(deque(maxlen=512))
            green_index += 1
            red_points.append(deque(maxlen=512))
            red_index += 1
            yellow_points.append(deque(maxlen=512))
            yellow_index += 1

        elif center[1] <= 65:
            if 40 <= center[0] <= 140: # Clear Button
                blue_points = [deque(maxlen=512)]
                green_points = [deque(maxlen=512)]
                red_points = [deque(maxlen=512)]
                yellow_points = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0

                whitecanvas[67:,:,:] = 255
            elif 160 <= center[0] <= 255:
                    colorIndex = 0 # Blue
            elif 275 <= center[0] <= 370:
                    colorIndex = 1 # Green
            elif 390 <= center[0] <= 485:
                    colorIndex = 2 # Red
            elif 505 <= center[0] <= 600:
                    colorIndex = 3 # Yellow
        else :
            if colorIndex == 0:
                blue_points[blue_index].appendleft(center)
            elif colorIndex == 1:
                green_points[green_index].appendleft(center)
            elif colorIndex == 2:
                red_points[red_index].appendleft(center)
            elif colorIndex == 3:
                yellow_points[yellow_index].appendleft(center)
    else:
        blue_points.append(deque(maxlen=512))
        blue_index += 1
        green_points.append(deque(maxlen=512))
        green_index += 1
        red_points.append(deque(maxlen=512))
        red_index += 1
        yellow_points.append(deque(maxlen=512))
        yellow_index += 1

    points = [blue_points, green_points, red_points, yellow_points]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(userwindow, points[i][j][k - 1], points[i][j][k], colorslist[i], 2)
                cv2.line(whitecanvas, points[i][j][k - 1], points[i][j][k], colorslist[i], 2)

    cv2.imshow("Output", userwindow)
    cv2.imshow("Paint", whitecanvas)

    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()