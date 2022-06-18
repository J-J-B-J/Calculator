import unittest

import process


class TestProcess(unittest.TestCase):
    def test_replace_symbols_pi(self):
        text = process._replace_symbols("π")
        self.assertEqual(text, "3.141592653589793")

    def test_replace_symbols_e(self):
        text = process._replace_symbols("℮")
        self.assertEqual(text, "2.718281828459045")

    def test_needs_processing_empty(self):
        needs_processing = process._needs_processing("")
        self.assertFalse(needs_processing)

    def test_needs_processing_plus(self):
        needs_processing = process._needs_processing("1+2")
        self.assertTrue(needs_processing)

    def test_needs_processing_minus(self):
        needs_processing = process._needs_processing("1-2")
        self.assertTrue(needs_processing)

    def test_needs_processing_times(self):
        needs_processing = process._needs_processing("1*2")
        self.assertTrue(needs_processing)

    def test_needs_processing_divide(self):
        needs_processing = process._needs_processing("1/2")
        self.assertTrue(needs_processing)

    def test_needs_processing_power(self):
        needs_processing = process._needs_processing("1^2")
        self.assertTrue(needs_processing)

    def test_get_operation_plus(self):
        operation = process._get_operation("1+2-3")
        self.assertEqual(operation, "+")

    def test_get_operation_minus(self):
        operation = process._get_operation("1-2+3")
        self.assertEqual(operation, "-")

    def test_get_operation_times(self):
        operation = process._get_operation("1*2+3-4/5")
        self.assertEqual(operation, "*")

    def test_get_operation_divide(self):
        operation = process._get_operation("1/2+3-4*5")
        self.assertEqual(operation, "/")

    def test_get_operation_power(self):
        operation = process._get_operation("1^2+3-4*5/6")
        self.assertEqual(operation, "^")


if __name__ == '__main__':
    unittest.main()
