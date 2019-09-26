import sys

def list_mean(L):
    try:
        return sum(L)/len(L)

    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)

def list_stdev(L):
    return None
