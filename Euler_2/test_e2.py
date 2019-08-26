import unittest
from e2 import sum_even_fibonacci


class TestEuler2(unittest.TestCase):
    def test_max(self):
        self.assertEqual(sum_even_fibonacci(50), 44)

if __name__ == "__main__":
    unittest.main()