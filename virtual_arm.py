

import cv2
import numpy as np

def draw_arm(canvas, angle_x, angle_y):
    base_center = (300, 420)

    base_size = 100
    column_height = 140
    arm_length = 160

    theta = np.radians(angle_x)   # rotation (ONLY arm)
    phi = np.radians(angle_y)     # up/down

    
    cv2.rectangle(canvas,
                (base_center[0] - base_size//2, base_center[1] - base_size//2),
                (base_center[0] + base_size//2, base_center[1] + base_size//2),
                (60,60,60), -1)

    
    column_top = (base_center[0], base_center[1] - column_height)

    cv2.line(canvas, base_center, column_top, (120,120,120), 20)

    
    cv2.circle(canvas, column_top, 12, (40,40,40), -1)

    
    x_end = int(column_top[0] + arm_length * np.cos(phi) * np.sin(theta))
    y_end = int(column_top[1] - arm_length * np.sin(phi))

    cv2.line(canvas, column_top, (x_end, y_end), (0,180,255), 12)
    cv2.line(canvas, column_top, (x_end, y_end), (0,120,200), 4)

    cv2.circle(canvas, (x_end, y_end), 8, (0,0,0), -1)