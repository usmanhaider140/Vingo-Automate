import testtools as testtools
import sys
import os
sys.path.append(os.path.join(sys.path[0], "../.."))
print(sys.path)


from  Test.Scripts.test_Login import Login

from unittest import TestLoader, TestSuite, TextTestRunner



if __name__ == "__main__":

    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Login),
     
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    parallel_suite = testtools.ConcurrentStreamTestSuite(
        lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
