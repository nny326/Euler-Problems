import unittest
from e4 import palindromer


class TestEuler4(unittest.TestCase):
    def test_palindromer(self):
        self.assertEqual(palindromer(2), 9009)


if __name__ == "__main__":
    unittest.main()
