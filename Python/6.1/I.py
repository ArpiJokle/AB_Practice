import numpy as np


def rotate(A, a):
    return np.rot90(A, (360 - a) // 90)