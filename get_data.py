import sys

def read_stdin_col(col_num):
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