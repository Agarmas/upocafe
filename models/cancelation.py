# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cancelation(models.Model):
    _name = 'upocafe.cancelation'
    _description = 'Payment cancelation'

    name = fields.Char(string='Cancelation name', required=True, help='name of the payment cancelation motive')
    motive = fields.Text(string='Cancelation motive', required=False, help='motive for payment cancelation')
    payments = fields.Many2one('upocafe.payment', string='Payments')
