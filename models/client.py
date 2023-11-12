from odoo import models, fields, api

class Client(models.Model):
    _inherit = 'res.partner'

    payment_ids = fields.one2Many("upocafe.payment",string="Uses")