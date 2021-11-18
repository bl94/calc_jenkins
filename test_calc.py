import unittest
import calc_jenkins

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc_jenkins.add(4,5),9)
    
    def test_multiply(self):
        self.assertEqual(calc_jenkins.multiply(4,5),20)
    
    def test_divide(self):
        self.assertEqual(calc_jenkins.divide(10,5),2)
    
    def test_subtract(self):
        self.assertEqual(calc_jenkins.subtract(10,5),5)

if __name__=='__main__':
    unittest.main()