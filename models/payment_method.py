# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PaymentMethod(models.Model):
     _name = 'upocafe.payment_method'
     _description = 'Method Payment'

     name = fields.Char(string='Payment method name', required=True, help='name of the payment method')
     payments = fields.One2many('upocafe.payment', string='Payments')
