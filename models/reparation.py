# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reparation(models.Model):
     _name = 'upocafe.reparation'
     _description = 'Reparation'

     start_datetime = fields.Datetime(string='Start of reparation date/time', required=True, autodate=True)
     end_datetime = fields.Datetime(string='End of reparation date/time', required=True)
     description = fields.Text(string='Description')
     machine_id = fields.Many2one('upocafe.machine', string='Machine')
     employee_ids = fields.Many2many('upocafe.employee', string='Employees')
