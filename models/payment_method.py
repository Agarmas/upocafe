# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PaymentMethod(models.Model):
     _name = 'upocafe.payment_method'
     _description = 'Method Payment'

     name = fields.Char(string='Nombre', required=True, help='Nombre del método de pago')
     payment_ids = fields.One2many('upocafe.payment', string='Pagos')
