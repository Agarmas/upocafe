# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reposition(models.Model):
     _inherit = "purchase.order.line"

     machine_id = fields.Many2one('upocafe.machine', string='Máquina', required = True)