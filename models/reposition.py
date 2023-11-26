# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reposition(models.Model):
     _inherit = "purchase.order"

     machine_id = fields.Many2one('upocafe.machine', string='Máquina')