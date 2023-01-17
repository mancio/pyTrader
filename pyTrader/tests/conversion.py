import unittest
import pyTrader.constants.indexes as ind
import pyTrader.constants.conversion_ratio as ratio
import pyTrader.tools.ticker as tk
import pyTrader.tools.conversion as conv

YAHOO = 11541.48
XTB = 11606.69


class Tests(unittest.TestCase):

    def test_conversion_smaller_to_bigger(self):
        current = conv.get_stock_from_ratio(YAHOO, ratio.US100_YAHOO_XTB)
        self.assertEqual(current, XTB)

    def test_conversion_bigger_to_smaller(self):
        current = conv.get_stock_from_ratio(XTB, ratio.US100_XTB_YAHOO)
        self.assertEqual(current, YAHOO)
