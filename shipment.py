# This file is part of stock_shipment_deviation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import Workflow, ModelView
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction
from trytond.wizard import Button, StateTransition, StateView, Wizard

__all__ = ['ShipmentOut', 'ShipmentDeviationAlert',
    'ShipmentDeviation']
__metaclass__ = PoolMeta


class ShipmentOut:
    __name__ = 'stock.shipment.out'

    @classmethod
    @ModelView.button_action('stock_shipment_deviation.deviation_wizard')
    @Workflow.transition('done')
    def done(cls, shipments):
        pool = Pool()
        Move = pool.get('stock.move')
        for shipment in shipments:
            outgoing_moves = [m.id for m in shipment.outgoing_moves]
            for move in shipment.inventory_moves:
                out_moves = Move.search([
                        ('id', 'in', outgoing_moves),
                        ('product', '=', move.product),
                        ('uom', '=', move.uom),
                        ])
                qty_shipped = reduce(lambda x, y: x + y,
                    [m.quantity for m in out_moves])
                origins = [o.origin for o in out_moves if o.origin]
                if origins:
                    qty_ordered = reduce(lambda x, y: x + y,
                        set([sl.quantity for sl in origins]))
                    if qty_shipped > qty_ordered:
                        moves_without_origin = [o for o in out_moves
                            if not o.origin]
                        Move.write(moves_without_origin,
                            {'origin': str(origins[0])})
        super(ShipmentOut, cls).done(shipments)


class ShipmentDeviationAlert(ModelView):
    'Shipment Deviation Alert'
    __name__ = 'shipment.deviation.alert'


class ShipmentDeviation(Wizard):
    'Shipment Deviation'
    __name__ = 'shipment.deviation'
    start = StateTransition()
    alert = StateView('shipment.deviation.alert',
        'stock_shipment_deviation.deviation_alert_view_form', [
            Button('Accept', 'end', 'tryton-ok', default=True),
            ])

    def transition_start(self, values=False):
        pool = Pool()
        Shipment = pool.get(Transaction().context['active_model'])
        Move = pool.get('stock.move')
        active_ids = Transaction().context['active_ids']
        for shipment in Shipment.browse(active_ids):
            outgoing_moves = [m.id for m in shipment.outgoing_moves]
            for move in shipment.inventory_moves:
                out_moves = Move.search([
                        ('id', 'in', outgoing_moves),
                        ('product', '=', move.product),
                        ('uom', '=', move.uom),
                        ])
                qty_shipped = reduce(lambda x, y: x + y,
                    [m.quantity for m in out_moves])
                origins = set([o.origin for o in out_moves])
                qty_ordered = reduce(lambda x, y: x + y,
                    [o.quantity for o in origins])
                if qty_shipped > qty_ordered:
                    return 'alert'
        return 'end'
