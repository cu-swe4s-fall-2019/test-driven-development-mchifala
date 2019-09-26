import unittest
from math_lib import list_mean
from math_lib import list_stdev
import random
import os
import numpy as np
import sys

class TestMath(unittest.TestCase):
    
    def test_mean_empty(self):
        self.assertRaises(ZeroDivisionError and
                          SystemExit, list_mean, [])
    
    def test_mean(self):
        for i in range(100):
            self.L = np.random.randint(0, 100, size=100)
            self.assertEqual(list_mean(self.L), np.mean(self.L))
        
    
    
if __name__ == '__main__':
    unittest.main()