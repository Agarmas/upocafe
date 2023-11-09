from odoo import models, fields

class order(models.Model):
    _name = order
    _inherit = "pos.order"
