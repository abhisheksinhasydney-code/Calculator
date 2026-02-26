"""Unit tests for calculator operations."""

import unittest

from calculator.operations import add, divide, multiply, subtract


class TestOperations(unittest.TestCase):
    """Test cases for arithmetic operation functions."""

    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(6, 7), 42)

    def test_divide(self) -> None:
        self.assertEqual(divide(20, 5), 4)

    def test_divide_by_zero_raises_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
