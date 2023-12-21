from odoo import models, fields, api


class Reparation(models.Model):
     _name = 'upocafe.reparation'
     _description = 'Reparation'

     machine_id = fields.Many2one('upocafe.machine', string='Máquina', require=True)
     name = fields.Text(string='Resumen', required=True)
     description = fields.Text(string='Descripción técnica')
     started = fields.Datetime(string='Comenzada', autodate=True, required=True)
     ended = fields.Datetime(string='Finalizada')
     employee_ids = fields.Many2many('hr.employee', string='Empleados', required=True)

     @api.onchange('started', 'ended')
     def _onchange_started_ended(self):
          if self.started:
               if not fields.Date.from_string(self.started):
                    return {
                         'value': {'started': ''},
                         'warning': {
                              'title': 'Formato de fecha incorrecto',
                              'message': 'El formato de la fecha no es válido. Utiliza el formato YYYY-MM-DD.'
                         }
                    }
               if not fields.Date.from_string(self.ended):
                    return {
                         'value': {'ended': ''},
                         'warning': {
                              'title': 'Formato de fecha incorrecto',
                              'message': 'El formato de la fecha no es válido. Utiliza el formato YYYY-MM-DD.'
                         }
                    }
               if self.started and self.ended and (self.started >= self.ended):
                    return {
                         'value': {'ended': ''},
                         'warning': {
                              'title': '¿Tratas de viajar en el tiempo?',
                              'message': 'La fecha de finalización no puede ser anterior a la fecha de inicio.'
                         }
                    }
          return {}
