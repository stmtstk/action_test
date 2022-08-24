""" test.py for main.py"""
import unittest
from codecov.src import main


class TestMethods(unittest.TestCase):
    """ Test Class"""
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_func_1_case_1(self) -> None:
        """ func_1, success """
        self.assertEqual(main.func_1(10), 10)

    def test_func_1_case_2(self) -> None:
        """ func_1, fail """
        self.assertEqual(main.func_1(10), 10)

    #def test_func_2_case_1(self) -> None:
    #    """ func_2, success """
    #    self.assertEqual(main.func_2(10), 10)

    #def test_func_2_case_2(self) -> None:
    #    """ func_2, fail """
    #    self.assertEqual(main.func_2(10), 10)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(TestMethods)
