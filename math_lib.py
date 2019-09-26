import sys
import math
import numpy as np


def list_mean(L):
    """
    This function calculates the mean of a list of numbers. It is \
    capable of handling errors when the list is empty or contains \
    the wrong data types.

    Parameters:
    - L(list): A list of numbers

    Returns:
    - mean(float): The mean of the list

    """
    try:
        return sum(L)/len(L)

    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)

    except TypeError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)


def list_stdev(L):
    """
    This function calculates the standard of a list of numbers. It is \
    capable of handling errors when the list is empty or contains \
    the wrong data types.

    Parameters:
    - L(list): A list of numbers

    Returns:
    - mean(float): The mean of the list

    """
    try:
        return math.sqrt(sum([(np.mean(L)-x)**2 for x in L]) / len(L))

    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)

    except TypeError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)
