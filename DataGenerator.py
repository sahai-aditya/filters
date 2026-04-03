import math
from random import uniform


def get_noisy_sin(a, T):
    """
    Returns a tuple of list of noisy sin data with amplitude a and time period T along with time list.
    """
    data = []
    time = []

    sin_func = lambda x: a * math.sin(x) # x here is in radian

    for t in range(0, 1001, 10): # t is in ms
        radians = 2 * math.pi * t / (T * 1000) # t converted to s from ms
        data.append(sin_func(radians) + uniform(-a / 10, a / 10))
        time.append(t)

    return data, time
