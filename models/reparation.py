# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reparation(models.Model):
     _name = 'upocafe.reparation'
     _description = 'Reparation'

     init_datetime = fields.Datetime(string='Comenzada', required=True, autodate=True)
     fini_datetime = fields.Datetime(string='Finalizada', required=True)
     repair_summary = fields.Text(string='Resumen', required=True)
     repair_description = fields.Text(string='Descripción Técnica', required=True)
     machine_id = fields.Many2one('upocafe.machine', string='Máquina')
     employee_ids = fields.Many2many('hr.employee', string='Empleados')
