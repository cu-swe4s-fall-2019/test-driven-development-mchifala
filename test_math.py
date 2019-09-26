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

    def test_mean_random_int(self):
        for i in range(100):
            self.L = np.random.randint(0, 100, size=100)
            self.assertEqual(list_mean(self.L), np.mean(self.L))

    def test_std_empty(self):
        self.assertRaises(ZeroDivisionError and
                          SystemExit, list_stdev, [])

    def test_std_random_int(self):
        for i in range(100):
            self.L = np.random.randint(0, 100, size=100)
            self.assertAlmostEqual(list_stdev(self.L), np.std(self.L))

    def test_mean_random_mix(self):
        for i in range(100):
            self.L = np.random.randint(0, 100, size=50)
            self.L = np.append(self.L, np.random.rand(50))
            self.assertAlmostEqual(list_mean(self.L), np.mean(self.L))

    def test_std_random_mix(self):
        for i in range(100):
            self.L = np.random.randint(0, 100, size=50)
            self.L = np.append(self.L, np.random.rand(50))
            self.assertAlmostEqual(list_stdev(self.L), np.std(self.L))

    def test_mean_string(self):
        self.assertRaises(TypeError and
                          SystemExit, list_mean, [3, "A"])

    def test_std_string(self):
        self.assertRaises(TypeError and
                          SystemExit, list_stdev, [3, "A"])

    def test_mean_string(self):
        self.assertRaises(TypeError and
                          SystemExit, list_mean, [3, None])

    def test_mean_string(self):
        self.assertRaises(TypeError and
                          SystemExit, list_stdev, [3, None])


if __name__ == '__main__':
    unittest.main()
