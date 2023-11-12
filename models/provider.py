from odoo import models, fields, api

class Provider(models.Model):
     _inherit = 'res.partner'

     reposition_ids = fields.One2many("purchase.order",string="Used material")