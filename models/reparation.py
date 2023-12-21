from odoo import models, fields, api


class Reparation(models.Model):
     _name = 'upocafe.reparation'
     _description = 'Reparation'

     name = fields.Text(required=True, string='Resumen', help='Resumen de la causa de la reparación')
     description = fields.Text(string='Descripción técnica', help='Descripción de la causa de la reparación para los empleados involucrados')
     started = fields.Datetime(default=fields.Datetime.now(), required=True, string='Comenzada', help='Fecha de inicio de la reparación')
     ended = fields.Datetime(string='Finalizada', help='Fecha de finalización de la reparación')
     machine_id = fields.Many2one('upocafe.machine', required=True, string='Máquina', help='Máquina afectada por la reparación')
     employee_ids = fields.Many2many('hr.employee', required=True, string='Empleados', help='Empleados involucrados')

     @api.onchange('started', 'ended')
     def _onchange_started_ended(self):
          if self.started and self.ended and (self.started >= self.ended):
               return {
                    'value': {'ended': ''},
                    'warning': {
                         'title': '¿Tratas de viajar en el tiempo?',
                         'message': 'La fecha de finalización no puede ser anterior a la fecha de inicio.'
                    }
               }
          return {}

     def btn_end_reparation(self):
          if not self.ended:
               now = fields.Datetime.now()
               self.write({'ended': now})
