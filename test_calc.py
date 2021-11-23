import unittest

import pytest

import calc_jenkins

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc_jenkins.add(4,5),9)
        #result=calc_jenkins.add(4,5)
        #assert result == 9
        

    def test_multiply(self):
        self.assertEqual(calc_jenkins.multiply(4,5),20)
        #result=calc_jenkins.multiply(4,5)
        #assert result == 20

    def test_divide(self):
        self.assertEqual(calc_jenkins.divide(10,5),2)
        #result=calc_jenkins.multiply(4,5)
        #assert result == 20

    def test_subtract(self):
        self.assertEqual(calc_jenkins.subtract(10,5),5)
        #result=calc_jenkins.multiply(4,5)
        #assert result == 20

if __name__=="__main__":
    unittest.main()