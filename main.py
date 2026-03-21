
import cv2
import time
import numpy as np

from hand_tracking import get_hand_position
from utils import map_value, smooth
from virtual_arm import draw_arm
import config


last_x, last_y = 0, 0   
mode = None

cap = cv2.VideoCapture(0)
cap.set(3, config.FRAME_WIDTH)
cap.set(4, config.FRAME_HEIGHT)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    x, y, fingers = get_hand_position(frame)

    if x is not None:

        if fingers == 2:
            mode = "lift"
        elif fingers == 1:
            mode = "rotate"


        if mode == "rotate":
            angle_x = map_value(x, 0, config.FRAME_WIDTH, -120, 120)
            angle_y = last_y

        
        elif mode == "lift":
            norm_y = y / config.FRAME_HEIGHT


            angle_y = (1 - norm_y) * 110 - 30

            angle_x = last_x

        else:
            angle_x, angle_y = last_x, last_y


        smooth_x, smooth_y = smooth(angle_x, angle_y, config.SMOOTHING)

        last_x, last_y = smooth_x, smooth_y

    else:
        smooth_x, smooth_y = last_x, last_y

    
    canvas = np.zeros((600, 600, 3), dtype=np.uint8)

    draw_arm(canvas, smooth_x, smooth_y)

    
    frame = cv2.resize(frame, (600, 600))
    combined = np.hstack((frame, canvas))

    cv2.imshow("🤖 Industrial Robot Arm Control", combined)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    time.sleep(0.01)

cap.release()
cv2.destroyAllWindows()