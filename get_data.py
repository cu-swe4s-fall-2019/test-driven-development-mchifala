import sys


def read_stdin_col(col_num):
    """
    This function reads in a column from stdin and returns a list of values \
    It handles the error when the column does not exist

    Parameters:
    - col_num: The column of stdin we wish to read

    Returns:
    L(list): A list of values

    """
    L = []
    for line in sys.stdin:
        line = line.strip().split()

        try:
            L.append(int(line[col_num]))

        except IndexError as inst:
            print("Run-Time Error:", type(inst))
            sys.exit(1)

    return L


if __name__ == '__main__':
    read_stdin_col(0)
