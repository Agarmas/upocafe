from odoo import models, fields

class Payment(models.Model):
    _name = 'upocafe.payment'
    _description = 'Pago de un conjunto de productos'

    id = fields.Char(string='Payment ID', required=True)
    date = fields.Date(string='Fecha')
    amount = fields.Float(string='Cantidad')
    payment_method_id = fields.Many2one('upocafe.payment_method', string='Metodo de pago')
    partner_id = fields.Many2one('res.partner', string='Cliente')
    currency_id = fields.Many2one('res.currency', string='Moneda')
    cancelation_id = fields.Many2one('upocafe.cancelation', string='Cancelacion')
    product_ids = fields.Many2many('product.product', string='Productos')
