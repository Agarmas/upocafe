from odoo import models, fields, api


class Machine(models.Model):
    _name = 'upocafe.machine'
    _description = 'Coffee vending machines'

    name = fields.Char(string="Nombre del modelo", size=255 ,required=True, help="name of the model")
    location = fields.Char('Localizacion', size=255, required=True, help="machines location")
    create_date = fields.Datetime('Fecha del alta',required=True, autodate = True)
    status_id = fields.Many2one("upocafe.status",string="Estado actual")
    #order_ids = fields.One2many("purchase.order",string="Machines repostions")
    reparations_ids = fields.One2many("upocafe.reparation", 'machine_id', string="Machines reparations")
    payments_ids = fields.One2many("upocafe.payment", 'machine_id', string="Machines payments")
    products_ids = fields.Many2many("product.product", string="Machines products")

    @api.onchange('create_date')
    def onchange_date(self):
        resultado = {}
        if self.create_date and not self._is_valid_date_format(self.create_date):
            resultado = {
                'value': {'create_date': ''},
                'warning': {
                    'title': 'Formato de fecha incorrecto',
                    'message': 'El formato de la fecha no es válido. Utiliza el formato YYYY-MM-DD.'
                }
            }
        return resultado

    def _is_valid_date_format(self, date_string):
        try:
            fields.Date.from_string(date_string)
            return True
        except ValueError:
            return False

    def btn_setDate(self):
        # Fijar el campo date a la fecha de hoy
        today_date = fields.Date.today()
        self.write({'create_date': today_date})
        
        return {
            'type': 'ir.actions.client',
            'tag': 'reload', 
        }

    def btn_generate_report(self):
        return self.env.ref('upocafe.machines_report').report_action(self)