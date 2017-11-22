import unittest
from code import is_even


class Test(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(4))

    def test_false(self):
        self.assertTrue(is_even(5))


if __name__ == '__main__':
    unittest.main()
