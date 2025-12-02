import unittest
from day1 import *

class Testcalczero(unittest.TestCase):
    def test_calc_zero(self):
        input = ['R101']
        self.assertEqual(calc_zero(input), 1)
        input2 = ['L101']
        self.assertEqual(calc_zero(input2), 1)

        input3 = ['L1001']
        self.assertEqual(calc_zero(input3), 10)

        input4 = ['R51', 'R99', 'R1']
        self.assertEqual(calc_zero(input4), 2)

        input5 = ['L51', 'L99', 'L1']
        self.assertEqual(calc_zero(input5), 2)

