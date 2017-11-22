import unittest
from code import is_even
from code import dependency_check


class Test(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(4))

    def test_false(self):
        self.assertFalse(is_even(5))

    def test_dependency(self):
        self.assertTrue(dependency_check('bcftools'))


if __name__ == '__main__':
    unittest.main()
