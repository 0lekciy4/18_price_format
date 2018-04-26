import unittest
from price_formater import format_price


class TestStringMethods(unittest.TestCase):

    def test_value(self):
        self.assertEqual(format_price('1000.000000'), '1 000')
        self.assertEqual(format_price('0.000000'), '0')
        self.assertEqual(format_price('999999.000000'), '999 999')
        self.assertEqual(format_price('999999.5555'), '999 999.56')
        self.assertEqual(format_price('ergtdf'), None)

    def test_types(self):
        self.assertEqual(str, type(format_price(423.00)))


if __name__ == '__main__':
    unittest.main()
