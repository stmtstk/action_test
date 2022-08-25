""" test.py for main.py"""
import unittest
from src.codecov.package.package_class import PackageClass


class TestMethods(unittest.TestCase):
    """ Test Class"""
    def setUp(self) -> None:
        self.pc = PackageClass()

    def tearDown(self) -> None:
        pass

    def test_func_1_success(self) -> None:
        """ func_1, success """
        self.assertEqual(self.pc.func_1(10), 10)

    #def test_func_11_success(self) -> None:
    #    """ func_1, success """
    #    self.assertEqual(self.pc.func_1(10), 10)

    #def test_func_1_fail(self) -> None:
    #    """ func_1, fail """
    #    self.assertEqual(self.pc.func_1(10), 20)

    def test_func_2_success(self) -> None:
        """ func_2, success """
        self.assertEqual(self.pc.func_2(10), 10)

    #def test_func_2_fail(self) -> None:
    #    """ func_2, fail """
    #    self.assertEqual(self.pc.func_2(10), 20)
