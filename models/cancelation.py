from odoo import models, fields, api


class Cancelation(models.Model):
    _name = 'upocafe.cancelation'
    _description = 'Payment cancelation'

    name = fields.Char(string='Nombre', required=True, help='Nombre de la cancelación del pago')
    motive = fields.Text(string='Motivo', required=False, help='Motivo de la cancelación del pago')
    payment_ids = fields.One2many('upocafe.payment', 'cancelation_id', string='Pagos')
    ncancelations = fields.Integer(compute='_totalCancelations', string='Total', store=True, help='Total de pagos afectados por este motivo de cancelación')
    
    def _totalCancelations(self):
        for record in self:
            record.ncancelations = len(record.payment_ids)
