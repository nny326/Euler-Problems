import unittest
from e1 import multiplies


class TestEuler1(unittest.TestCase):
    def test_negative_num(self):
        data = -10
        result = multiplies(data)
        self.assertEqual(result, 0)

    def test_positive_num(self):
        data = 10
        result = multiplies(data)
        self.assertEqual(result, 23)


if __name__ == "__main__":
    unittest.main()
