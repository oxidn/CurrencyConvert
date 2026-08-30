import unittest
from unittest.mock import patch
from src.converter import convert_currency


class TestCurrencyConverter(unittest.TestCase):

    @patch("src.converter.get_exchange_rates")
    def test_valid_conversion(self, mock_get_rates):
        mock_get_rates.return_value = {
            "USD": 1.0,
            "INR": 83.0,
            "EUR": 0.9
        }

        result = convert_currency(100, "USD", "INR")

        self.assertEqual(result, 8300.0)

    @patch("src.converter.get_exchange_rates")
    def test_conversion_between_currencies(self, mock_get_rates):
        mock_get_rates.return_value = {
            "USD": 1.0,
            "INR": 80.0,
            "EUR": 0.8
        }

        result = convert_currency(80, "INR", "EUR")

        self.assertEqual(result, 0.8)

    def test_negative_amount(self):
        with self.assertRaises(ValueError) as context:
            convert_currency(-100, "USD", "INR")

        self.assertEqual(
            str(context.exception),
            "Amount must be greater than zero."
        )

    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            convert_currency(0, "USD", "INR")

    @patch("src.converter.get_exchange_rates")
    def test_invalid_source_currency(self, mock_get_rates):
        mock_get_rates.return_value = {
            "USD": 1.0,
            "INR": 83.0
        }

        with self.assertRaises(ValueError) as context:
            convert_currency(100, "XYZ", "INR")

        self.assertEqual(
            str(context.exception),
            "Unsupported currency code: XYZ"
        )

    @patch("src.converter.get_exchange_rates")
    def test_invalid_target_currency(self, mock_get_rates):
        mock_get_rates.return_value = {
            "USD": 1.0,
            "INR": 83.0
        }

        with self.assertRaises(ValueError) as context:
            convert_currency(100, "USD", "XYZ")

        self.assertEqual(
            str(context.exception),
            "Unsupported currency code: XYZ"
        )


if __name__ == "__main__":
    unittest.main()