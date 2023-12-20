from odoo import models, fields, api


class PaymentMethod(models.Model):
     _name = 'upocafe.payment_method'
     _description = 'Method Payment'

     name = fields.Char(string='Nombre', required=True,
                        help='Nombre del método de pago')
     payment_ids = fields.One2many('upocafe.payment', 'payment_method_id',
                                   string='Pagos',
                                   help='Pagos realizados con \
                                        este método de pago')
     ntransactions = fields.Integer(compute='_totalTransactions',
                                   string='Pagos totales', store=True,
                                   help='Total de pagos realizados con \
                                        este método de pago')

     def _totalTransactions(self):
          for record in self:
               record.ntransactions = len(record.payment_ids)
