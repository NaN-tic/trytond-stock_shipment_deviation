# This file is part of the stock_shipment_deviation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockShipmentDeviationTestCase(ModuleTestCase):
    'Test Stock Shipment Deviation module'
    module = 'stock_shipment_deviation'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockShipmentDeviationTestCase))
    return suite
