import unittest
from math_lib import list_mean
from math_lib import list_stdev
import random
import os
import numpy as np

class TestMath(unittest.TestCase):
    
    def test_mean_empty(self):
        self.assertRaises(ZeroDivisionError and
                          SystemExit, list_mean, [])
    
if __name__ == '__main__':
    unittest.main()