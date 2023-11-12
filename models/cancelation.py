# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cancelation(models.Model):
    _name = 'upocafe.cancelation'
    _description = 'Payment cancelation'

    name = fields.Char(string='Nombre', required=True, help='Nombre de la cancelación del pago')
    motive = fields.Text(string='Motivo', required=False, help='Motivo de la cancelación del pago')
    payment_id = fields.Many2one('upocafe.payment', string='Pagos')
