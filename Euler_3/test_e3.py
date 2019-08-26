import unittest
from e3 import prime_generator


class TestEuler3(unittest.TestCase):
    def test_positive_num(self):
        self.assertEqual(prime_generator(13195), 29)

    def test_negative_number(self):
        self.assertEqual(prime_generator(-13195), 1)


if __name__ == "__main__":
    unittest.main()
