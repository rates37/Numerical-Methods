# Testing file for integral approximating methods 
# Author: Satya Jhaveri

import unittest
from rectangle_method import rectangle, rectangle_vec
from simpsons_13 import simpsons_13, simpsons_13_vec
from simpsons_38 import simpsons_38, simpsons_38_vec
from trapezoidal_method import trapezoidal, trapezoidal_vec


class TestIntegralApprox(unittest.TestCase):
    def setUp(self) -> None:
        # Create list of error to collect over all tests:
        self.errorList = []
    
    def tearDown(self) -> None:
        # Print all errors found:
        for e in self.errorList:
            print(e)
        print(f"Number of errors: {len(self.errorList)}")
    
    def test_rectangle(self) -> None:
        def f(x): return x*x
        acceptable_error = 0.1
        a,b = -5, 5
        n = 100000
        actual_value = 250/3
        # Testing method:
        try:
            self.assertGreaterEqual(acceptable_error, abs(actual_value - rectangle(f, a, b, n)), msg="Incorrect rectangle method")
        except AssertionError as e:
            self.errorList.append(str(e))

        # Passing invalid values to function:
        # testing invalid integral bounds:
        a, b = 1, 0  # Lower > upper
        try:
            self.assertRaises(ValueError, rectangle, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when lower integral bound > upper integral bound")
            
        # Testing invalid value of n:
        n = 0
        a, b = -5, 5
        try:
            self.assertRaises(ValueError, rectangle, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when number of points is less than 1")
    
    def test_rectangle_vec(self) -> None:
        def f(x): return x*x
        acceptable_error = 0.1
        
        a, b = -5, 5
        n = 1000000
        width = (b - a) / (n - 1)
        x = [a + i*width for i in range(n)]
        y = [f(i) for i in x]
        actual_value = 250/3
        
        try:
            self.assertGreaterEqual(acceptable_error, abs(rectangle_vec(x,y) - actual_value), msg="Rectangle method with vector input not working correctly")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        # Testing invalid inputs:
        x, y = [], [1]

        try:
            self.assertRaises(ValueError, rectangle_vec, x, y)
        except AssertionError:
            self.errorList.append("Rectangle method with vector input did not raise ValueError when input vectors are of different size")

    def test_trapezoidal(self) -> None:
        def f(x): return x*x
        acceptable_error = 0.1
        a,b = -5, 5
        n = 100000
        actual_value = 250/3
        # Testing method:
        try:
            self.assertGreaterEqual(acceptable_error, abs(actual_value - trapezoidal(f, a, b, n)), msg="Incorrect trapezoidal method")
        except AssertionError as e:
            self.errorList.append(str(e))

        # Passing invalid values to function:
        # testing invalid integral bounds:
        a, b = 1, 0  # Lower > upper
        try:
            self.assertRaises(ValueError, trapezoidal, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when lower integral bound > upper integral bound")
            
        # Testing invalid value of n:
        n = 0
        a, b = -5, 5
        try:
            self.assertRaises(ValueError, trapezoidal, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when number of points is less than 1")
    
    def test_trapezoidal_vec(self) -> None:
        def f(x): return x*x
        acceptable_error = 0.1
        
        a, b = -5, 5
        n = 1000000
        width = (b - a) / (n - 1)
        x = [a + i*width for i in range(n)]
        y = [f(i) for i in x]
        actual_value = 250/3
        
        try:
            self.assertGreaterEqual(acceptable_error, abs(trapezoidal_vec(x,y) - actual_value), msg="Trapezoidal method with vector input not working correctly")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        # Testing invalid inputs:
        x, y = [], [1]

        try:
            self.assertRaises(ValueError, trapezoidal_vec, x, y)
        except AssertionError:
            self.errorList.append("Trapezoidal method with vector input did not raise ValueError when input vectors are of different size")

    def test_simpsons_13(self) -> None:
        def f(x): return x*x
        acceptable_error = 0.1
        a,b = -5, 5
        n = 100001
        actual_value = 250/3
        # Testing method:
        try:
            self.assertGreaterEqual(acceptable_error, abs(actual_value - simpsons_13(f, a, b, n)), msg="Incorrect Simpson's 1/3 method")
        except AssertionError as e:
            self.errorList.append(str(e))

        # Passing invalid values to function:
        # testing invalid integral bounds:
        a, b = 1, 0  # Lower > upper
        try:
            self.assertRaises(ValueError, simpsons_13, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when lower integral bound > upper integral bound")
            
        # Testing invalid value of n:
        n = 0
        a, b = -5, 5
        try:
            self.assertRaises(ValueError, simpsons_13, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when number of points is less than 3")
        
        #Testing even value of n:
        n = 10
        try:
            self.assertRaises(ValueError, simpsons_13, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when number of points is even")
    
    def test_simpsons_13_vec(self) -> None:
        def f(x): return x*x
        acceptable_error = 0.1
        
        a, b = -5, 5
        n = 1000001
        width = (b - a) / (n - 1)
        x = [a + i*width for i in range(n)]
        y = [f(i) for i in x]
        actual_value = 250/3
        
        try:
            self.assertGreaterEqual(acceptable_error, abs(simpsons_13_vec(x,y) - actual_value), msg="Simpson's 1/3 method with vector input not working correctly")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        # Testing invalid inputs:
        x, y = [], [1]

        try:
            self.assertRaises(ValueError, simpsons_13_vec, x, y)
        except AssertionError:
            self.errorList.append("Simpson's 1/3 method with vector input did not raise ValueError when input vectors are of different size")
    
    def test_simpsons_38(self) -> None:
        def f(x): return x*x
        acceptable_error = 0.1
        a,b = -5, 5
        n = 100003
        actual_value = 250/3
        # Testing method:
        try:
            self.assertGreaterEqual(acceptable_error, abs(actual_value - simpsons_38(f, a, b, n)), msg="Incorrect Simpson's 3/8 method")
        except AssertionError as e:
            self.errorList.append(str(e))

        # Passing invalid values to function:
        # testing invalid integral bounds:
        a, b = 1, 0  # Lower > upper
        try:
            self.assertRaises(ValueError, simpsons_38, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when lower integral bound > upper integral bound")
            
        # Testing invalid value of n:
        n = 0
        a, b = -5, 5
        try:
            self.assertRaises(ValueError, simpsons_38, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when number of points is less than 4")
        
        #Testing value of n that is not congruent to 4 (mod 3):
        n = 11
        try:
            self.assertRaises(ValueError, simpsons_38, f, a, b, n)
        except AssertionError:
            self.errorList.append("ValueError not raised when number of points is not congruent to 4 (mod 3)")
        
    def test_simpsons_38_vec(self) -> None:
        def f(x): return x*x
        acceptable_error = 0.1
        
        a, b = -5, 5
        n = 1000003
        width = (b - a) / (n - 1)
        x = [a + i*width for i in range(n)]
        y = [f(i) for i in x]
        actual_value = 250/3
        
        try:
            self.assertGreaterEqual(acceptable_error, abs(simpsons_38_vec(x,y) - actual_value), msg="Simpson's 3/8 method with vector input not working correctly")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        # Testing invalid inputs:
        x, y = [0], [1]  # Not large enough vectors

        try:
            self.assertRaises(ValueError, simpsons_38_vec, x, y)
        except AssertionError:
            self.errorList.append("Simpson's 3/8 method with vector input did not raise ValueError when input vectors are too small")
        
        x, y = [1,2,3,4], [1,2,3]
        try:
            self.assertRaises(ValueError, simpsons_38_vec, x, y)
        except AssertionError:
            self.errorList.append("Simpson's 3/8 method with vector input did not raise ValueError when input vectors are different sizes")
    
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIntegralApprox)
    unittest.TextTestRunner(verbosity=0).run(suite)
