# Testing file for ordinary differential equation methods
# Author: Satya Jhaveri

import unittest



class TestODE(unittest.TestCase):
    def setUp(self) -> None:
        # Create list of error to collect over all tests:
        self.errorList = []
    
    def tearDown(self) -> None:
        # Print all errors found:
        for e in self.errorList:
            print(e)
        print(f"Number of errors: {len(self.errorList)}")
    
    
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestODE)
    unittest.TextTestRunner(verbosity=0).run(suite)
