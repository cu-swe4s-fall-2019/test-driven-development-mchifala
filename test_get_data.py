import unittest
from get_data import read_stdin_col
import numpy as np


class TestGetData(unittest.TestCase):
    
    test_stdin(self):
        for i in range(100):
            self.first = np.random.randint(0, 100, size=100)
            self.second = np.random.randint(0, 100, size=100)
            for i,j in zip(first, second):
                print "%s %s" % (i,j)
            assertListEqual(read_stdin_col(1), self.first)


if __name__ == '__main__':
    unittest.main()