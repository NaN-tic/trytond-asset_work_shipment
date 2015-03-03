# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .shipment import *
from .asset import *


def register():
    Pool.register(
        ShipmentWork,
        Asset,
        module='asset_work_shipment', type_='model')
