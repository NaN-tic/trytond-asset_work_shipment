# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['ShipmentWork']
__metaclass__ = PoolMeta


class ShipmentWork:
    __name__ = 'shipment.work'

    asset = fields.Many2One('asset', 'Asset')
