import sys
import math
import numpy as np


def list_mean(L):
    try:
        return sum(L)/len(L)

    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)

    except TypeError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)


def list_stdev(L):
    try:
        return math.sqrt(sum([(np.mean(L)-x)**2 for x in L]) / len(L))

    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)

    except TypeError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)
