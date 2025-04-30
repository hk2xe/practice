import unittest
from main import quadratic_equation


class TestQuadraticEquation(unittest.TestCase):

    def test_two_real_roots(self):
        result = quadratic_equation(1, -5, 6)
        self.assertAlmostEqual(result[0], 2.0)
        self.assertAlmostEqual(result[1], 3.0)

    def test_one_real_root(self):
        result = quadratic_equation(1, -4, 4)
        self.assertAlmostEqual(result, 2.0)

    def test_no_real_roots(self):
        result = quadratic_equation(1, 1, 1)
        self.assertEqual(result, "Нет корней")

    def test_a_zero(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 2, 1)

    def test_negative_a(self):
        result = quadratic_equation(-1, -2, 3)
        self.assertAlmostEqual(result[0], 1.0)
        self.assertAlmostEqual(result[1], -3.0)


if __name__ == "__main__":
    unittest.main()
