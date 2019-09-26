import matplotlib.pyplot as plt
import numpy as np
import os
from data_viz import boxplot
from data_viz import histogram
from data_viz import combo
import unittest
import matplotlib
matplotlib.use('Agg')


class TestPlots(unittest.TestCase):
    """
    This class is used to test the boxplot, histogram, and \
    combo methods from the data_viz module.

    """
    def test_histogram_exists(self):
        self.L = np.random.randint(0, 100, size=100)
        self.file = "histogram_test"
        histogram(self.L, self.file)
        self.assertEqual(True, os.path.exists(self.file+".png"))

    def test_histogram_not_exist(self):
        self.L = np.random.randint(0, 100, size=100)
        self.file = "histogram_test2"
        histogram(self.L, "bad_histogram")
        self.assertEqual(False, os.path.exists(self.file+".png"))

    def test_boxplot_exist(self):
        self.L = np.random.randint(0, 100, size=100)
        self.file = "boxplot_test"
        boxplot(self.L, self.file)
        self.assertEqual(True, os.path.exists(self.file+".png"))

    def test_boxplot_not_exist(self):
        self.L = np.random.randint(0, 100, size=100)
        self.file = "boxplot_test2"
        boxplot(self.L, "bad_boxplot")
        self.assertEqual(False, os.path.exists(self.file+".png"))

    def test_combo_exist(self):
        self.L = np.random.randint(0, 100, size=100)
        self.file = "combo_test"
        combo(self.L, self.file)
        self.assertEqual(True, os.path.exists(self.file+".png"))

    def test_combo_not_exist(self):
        self.L = np.random.randint(0, 100, size=100)
        self.file = "combo_test2"
        combo(self.L, "bad_combo")
        self.assertEqual(False, os.path.exists(self.file+".png"))


if __name__ == '__main__':
    unittest.main()
