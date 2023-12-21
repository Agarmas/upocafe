from odoo import models, fields, api


class Status(models.Model):
     _name = 'upocafe.status'
     _description = 'Status of a machine'

     name = fields.Selection([('activo','Activo'),
                              ('averiado','Averiado'),
                              ('en reparacion','En Reparacion'),],
                              'Estados de una maquina', default='activo')
     machines_ids = fields.One2many("upocafe.machine", 'status_id', string="Maquinas con este estado")
     
     def btn_status_to_activo(self):
          self.write({'name':'activo'})

     def btn_status_to_reparacion(self):
          self.write({'name':'en reparacion'})

     def btn_status_to_averiado(self):
          self.write({'name':'averiado'})