import numpy as np


def multiplication_matrix(a):
    N = np.arange(1, a + 1)
    return (N * N[:, None])