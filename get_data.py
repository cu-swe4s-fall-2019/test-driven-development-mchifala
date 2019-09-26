import sys

def read_stdin_col(col_num):
    L = []
    for line in sys.stdin:
        line = line.strip().split()
        L.append(int(line[col_num]))

    return L
        

if __name__ == '__main__':
    read_stdin_col(0)