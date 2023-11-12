from odoo import models, fields, api

class Reposition(models.Model):
     _inherit = 'purchase.order'

     provider_id = fields.Many2one("upocafe.provider",string="Provides")
     machine_id = fields.Many2one("upocafe.machine", string="Replenishes")