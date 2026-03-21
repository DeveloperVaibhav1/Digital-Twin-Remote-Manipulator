import numpy as np

prev_x, prev_y = 0, 0

def map_value(x, in_min, in_max, out_min, out_max):
    return int(np.interp(x, [in_min, in_max], [out_min, out_max]))

def smooth(x, y, alpha=0.2):
    global prev_x, prev_y

    smooth_x = prev_x * (1 - alpha) + x * alpha
    smooth_y = prev_y * (1 - alpha) + y * alpha

    prev_x, prev_y = smooth_x, smooth_y

    return int(smooth_x), int(smooth_y)