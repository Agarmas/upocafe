from odoo import models, fields, api


class Reparation(models.Model):
     _name = 'upocafe.reparation'
     _description = 'Reparation'

     machine_id = fields.Many2one('upocafe.machine', string='Máquina',
                                  required=True)
     name = fields.Text(string='Resumen', required=True)
     description = fields.Text(string='Descripción técnica')
     started = fields.Datetime(string='Comenzada', autodate=True,
                               required=True)
     ended = fields.Datetime(string='Finalizada')
     employee_ids = fields.Many2many('hr.employee', string='Empleados',
                                     required=True)
