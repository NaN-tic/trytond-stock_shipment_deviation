# This file is part of stock_shipment_deviation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .shipment import *


def register():
    Pool.register(
        ShipmentOut,
        ShipmentDeviationAlert,
        module='stock_shipment_deviation', type_='model')
    Pool.register(
        ShipmentDeviation,
        module='stock_shipment_deviation', type_='wizard')
