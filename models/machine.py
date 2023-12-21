from odoo import models, fields, api


class Machine(models.Model):
     _name = 'upocafe.machine'
     _description = 'Coffee vending machines'

     name = fields.Char(string="Nombre del modelo", size=255 ,required=True, help="name of the model")
     location = fields.Char('Localizacion', size=255, required=True, help="machines location")
     create_date = fields.Datetime('Fecha del alta',required=True, autodate = True)
     status_id = fields.Many2one("upocafe.status",string="Estado actual")
     repositions_ids = fields.One2many("purchase.order.line", 'machine_id', string="Machines repostions")
     reparations_ids = fields.One2many("upocafe.reparation", 'machine_id', string="Machines reparations")
     payments_ids = fields.One2many("upocafe.payment", 'machine_id', string="Machines payments")
     products_ids = fields.Many2many("product.product", string="Machines products")
