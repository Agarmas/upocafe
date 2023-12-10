from odoo import models, fields, api


class Status(models.Model):
     _name = 'upocafe.status'
     _description = 'Status of a machine'

     status = fields.Char(string="Estado", size=255 ,required=True, help="status of a machine")
     machines_ids = fields.One2many("upocafe.machine", 'status_id', string="Maquinas con este estado")