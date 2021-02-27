# Testing file for root finding methods 
# Author: Satya Jhaveri

import unittest
from bisection_method import bisection
from false_position import false_position
from newton_raphson import newton_raphson
from secant_method import secant


class TestRootFinding(unittest.TestCase):
    def setUp(self) -> None:
        # Create list of error to collect over all tests:
        self.errorList = []
    
    def tearDown(self) -> None:
        # Print all errors found:
        for e in self.errorList:
            print(e)
        print(f"Number of errors: {len(self.errorList)}")

    def test_bisection(self) -> None:
        def f(x: float) -> float: return (x-1) * (x+6)
        precision = 0.0001
        
        # Finding the left root (x = -6):
        lower, upper = -10, 0
        actual_root = -6
        approximated_root = bisection(f, lower, upper, precision)
        
        try:
            self.assertGreaterEqual(precision, abs(approximated_root - actual_root), msg=f"Not precise enough:\n\tActual Root = {actual_root}, Approximated Root = {approximated_root}")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        
        # Finding the right root (x = 1):
        lower, upper = 0, 10
        actual_root = 1
        approximated_root = bisection(f, lower, upper, precision)
        try:
            self.assertGreaterEqual(precision, abs(approximated_root - actual_root), msg=f"Not precise enough:\n\tActual Root = {actual_root}, Approximated Root = {approximated_root}")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        
        # Passing invalid values to function:
        # Invalid values of lower and upper:
        lower, upper = 0, 0  # Lower = upper
        try:
            self.assertRaises(ValueError, bisection, f, lower, upper, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when lower == upper")
            
        lower, upper = -20,-10  # f(lower) and f(upper) have same sign
        try:
            self.assertRaises(ValueError, bisection, f, lower, upper, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when f(lower) and f(upper) have same sign")
        
        # Negative Precision
        lower, upper = 0, 10
        precision = -0.12345
        try:
            self.assertRaises(ValueError, bisection, f, lower, upper, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when precision <= 0")

    def test_false_position(self) -> None:
        def f(x: float) -> float: return (x-1) * (x+6)
        precision = 0.0001
        
        # Finding the left root (x = -6):
        lower, upper = -10, 0
        actual_root = -6
        approximated_root = false_position(f, lower, upper, precision)
        
        try:
            self.assertGreaterEqual(precision, abs(approximated_root - actual_root), msg=f"Not precise enough:\n\tActual Root = {actual_root}, Approximated Root = {approximated_root}")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        
        # Finding the right root (x = 1):
        lower, upper = 0, 10
        actual_root = 1
        approximated_root = false_position(f, lower, upper, precision)
        try:
            self.assertGreaterEqual(precision, abs(approximated_root - actual_root), msg=f"Not precise enough:\n\tActual Root = {actual_root}, Approximated Root = {approximated_root}")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        
        # Passing invalid values to function:
        # Invalid values of lower and upper:
        lower, upper = 0, 0  # Lower = upper
        try:
            self.assertRaises(ValueError, false_position, f, lower, upper, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when lower == upper")
            
        lower, upper = -20,-10  # f(lower) and f(upper) have same sign
        try:
            self.assertRaises(ValueError, false_position, f, lower, upper, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when f(lower) and f(upper) have same sign")
        
        # Negative Precision
        lower, upper = 0, 10
        precision = -0.12345
        try:
            self.assertRaises(ValueError, false_position, f, lower, upper, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when precision <= 0")

    def test_newton_raphson(self) -> None:
        def f(x: float) -> float: return (x-1) * (x+6)
        def df(x: float) -> float: return 2 * x + 5
        precision = 0.0001

        # Finding the left root (x = -6):
        initial = -10
        actual_root = -6
        approximated_root = newton_raphson(f, df, initial, precision)
        
        try:
            self.assertGreaterEqual(precision, abs(approximated_root - actual_root), msg=f"Not precise enough:\n\tActual Root = {actual_root}, Approximated Root = {approximated_root}")
        except AssertionError as e:
            self.errorList.append(str(e))

        # Finding the right root:
        initial = 10
        precision = 0.0001
        actual_root = 1
        approximated_root = newton_raphson(f, df, initial, precision)
        
        try:
            self.assertGreaterEqual(precision, abs(approximated_root - actual_root), msg=f"Not precise enough:\n\tActual Root = {actual_root}, Approximated Root = {approximated_root}")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        # Passing Invalid Values:
        # Negative Precision:
        precision = -0.12345
        try:
            self.assertRaises(ValueError, newton_raphson, f, df, initial, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when precision <= 0")

    def test_secant(self) -> None:
         # Basic testing:
        precision = 0.0001

        def f(x: float) -> float: return (x-1) * (x+6)

        # Finding the left root (x = -6):
        x1, x2 = -10, -5
        actual_root = -6
        approximated_root = secant(f, x1, x2, precision)
        try:
            self.assertGreaterEqual(precision, abs(approximated_root - actual_root), msg=f"Not precise enough:\n\tActual Root = {actual_root}, Approximated Root = {approximated_root}")
        except AssertionError as e:
            self.errorList.append(str(e))

        # Finding the right root:
        x1, x2 = 0, 5
        precision = 0.0001
        actual_root = 1
        approximated_root = secant(f, x1, x2, precision)
        try:
            self.assertGreaterEqual(precision, abs(approximated_root - actual_root), msg=f"Not precise enough:\n\tActual Root = {actual_root}, Approximated Root = {approximated_root}")
        except AssertionError as e:
            self.errorList.append(str(e))
        
        # Passing invalid values to function:
        # Invalid values of x1 and x2:
        x1, x2 = 0, 0  # x1 = x2
        try:
            self.assertRaises(ValueError, secant, f, x1, x2, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when x1 == x2")
            
        x1, x2 = -20,-10  # f(x1) and f(x2) have same sign
        try:
            self.assertRaises(ValueError, secant, f, x1, x2, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when f(x1) and f(x2) have same sign")
        
        # Negative Precision
        x1, x2 = 0, 10
        precision = -0.12345
        try:
            self.assertRaises(ValueError, secant, f, x1, x2, precision)
        except AssertionError as e:
            self.errorList.append("ValueError not raised when precision <= 0")
        pass
    
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRootFinding)
    unittest.TextTestRunner(verbosity=0).run(suite)
