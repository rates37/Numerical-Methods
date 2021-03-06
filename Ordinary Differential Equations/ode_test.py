# Testing file for ordinary differential equation methods
# Author: Satya Jhaveri

import unittest
from math import exp
from euler import forward_euler


class TestODE(unittest.TestCase):
    def setUp(self) -> None:
        # Create list of error to collect over all tests:
        self.errorList = []
    
    def tearDown(self) -> None:
        # Print all errors found:
        for e in self.errorList:
            print(e)
        print(f"Number of errors: {len(self.errorList)}")
        
    def testEuler(self) -> None:
        def f(x,y):
            return y
        
        precision = 0.01
        
        
        # Testing method:
        start_x, end_x = 0,4
        start_y = 1
        n = 0.005
        x, y = forward_euler(f, start_x, end_x,start_y, n)
        actual_value = exp(4)
        
        try:
            self.assertLessEqual(y[-1] - actual_value, precision, msg="Forward Euler method not working accurately")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        # Testing invalid inputs:
        # When start x is higher than final x:
        try:
            self.assertRaises(ValueError, forward_euler, f, end_x, start_x, start_y, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when final x value is less than the initial x value")
        
        # Giving step value = 0:
        n = 0
        try:
            self.assertRaises(ValueError, forward_euler, f, start_x, end_x, start_y, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when step value = 0")
        
        # Giving step value < 0:
        n = -1
        try:
            self.assertRaises(ValueError, forward_euler, f, start_x, end_x, start_y, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when step value < 0")
        
    
    
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestODE)
    unittest.TextTestRunner(verbosity=0).run(suite)
