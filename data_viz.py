from math_lib import list_mean
from math_lib import list_stdev
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')


def boxplot(L, out_file_name):
    mean = list_mean(L)
    std = list_stdev(L)
    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    plt.boxplot(L)
    plt.title("Mean: " + str(mean) + " Standard Deviation: " + str(std))
    plt.xlabel("Array #1")
    plt.ylabel("Value")
    plt.savefig(out_file_name, bbox_inches='tight')


def histogram(L, out_file_name):
    mean = list_mean(L)
    std = list_stdev(L)
    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    plt.hist(L)
    plt.title("Mean: " + str(mean) + " Standard Deviation: " + str(std))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig(out_file_name, bbox_inches='tight')


def combo(L, out_file_name):
    width = 3
    height = 3
    mean = list_mean(L)
    std = list_stdev(L)
    fig, axes = plt.subplots(2, 1)
    axes[0].hist(L)
    axes[0].set_xlabel("Value")
    axes[0].set_ylabel("Frequency")
    axes[0].set_title("Mean: " + str(mean) + "Standard Deviation: " + str(std),
                      loc="right")
    axes[1].boxplot(L)
    axes[1].set_xlabel("Array #1")
    axes[1].set_ylabel("Value")
    axes[1].set_title("Mean: " + str(mean) + "Standard Deviation: " + str(std),
                      loc="right")
    plt.tight_layout()
    plt.savefig(out_file_name)

# if __name__ == '__main__':
    # histogram(np.random.randint(0,100,100), "test.png")
    # boxplot(np.random.randint(0,100,100), "test2.png")
    # combo(np.random.randint(0,100,100), "test3.png")
