from data_viz import boxplot
from data_viz import histogram
from data_viz import combo
from math_lib import list_mean
from math_lib import list_stdev
from get_data import read_stdin_col
import matplotlib.pyplot as plt
import numpy as np
import argparse
import matplotlib
matplotlib.use('Agg')


def main(out_file, col_num, plot_type):
    """
    This script generates either a boxplot, histogram, or combo plot \
    from a user selected column in stdin and saves it to an outfile

    Parameters:
    - outfile(str): The user-defined file name for the generated plot
    - col_num(int): The user-defined column number of interest
    - plot_type(str): The user-defined type of plot to generate

    Returns:
    - None, but a plot is generated and saved to a file

    """
    L = read_stdin_col(col_num)

    if plot_type == "boxplot":
        boxplot(L, out_file)

    elif plot_type == "histogram":
        histogram(L, out_file)

    if plot_type == "combo":
        combo(L, out_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Column stats input")

    parser.add_argument('--out_file',
                        type=str,
                        help='Name of the file (with extension)',
                        required=True)

    parser.add_argument('--col_num',
                        type=int,
                        help='Column number to be analyzed',
                        required=True)

    parser.add_argument('--plot_type',
                        type=str,
                        help='Type of plot to be generated',
                        required=True)

    args = parser.parse_args()
    main(args.out_file, args.col_num, args.plot_type)
