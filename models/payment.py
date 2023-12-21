from odoo import api, models, fields

class Payment(models.Model):
    _name = 'upocafe.payment'
    _description = 'Pago de un conjunto de productos'

    date = fields.Date(string='Fecha', required=True)
    amount = fields.Float(string='Precio', compute='_compute_amount', store=True)
    payment_method_id = fields.Many2one('upocafe.payment_method', string='Metodo de pago', required=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    currency_id = fields.Many2one('res.currency', string='Moneda', required=True)
    cancelation_id = fields.Many2one('upocafe.cancelation', string='Cancelacion')
    production_ids = fields.Many2many('mrp.production', string='Ordenes de producción')
    machine_id = fields.Many2one('upocafe.machine', string='Máquina', required=True)


    @api.depends('production_ids.product_qty', 'production_ids.product_id.lst_price')
    def _compute_amount(self):
        for record in self:
            record.amount = sum( (production.product_qty * production.product_id.lst_price) for production in record.production_ids)

    # Validaciones de la  fecha
    @api.onchange('date')
    def onchange_date(self):
        resultado = {}
        if self.date and not self._is_valid_date_format(self.date):
            resultado = {
                'value': {'date': ''},
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

    # Fin de las validaciones de la fecha

    # Método para "limpiar el carrito" de productos
    def btn_removeProductions(self):
        # Borramos los productos de este pago
        self.write({'production_ids':[(5,)]})
        
        # Borramos las ordenes de producción para no tener ordenes de producción invalidas
        production_orders = self.env['mrp.production'].search([('id', 'in', self.production_ids.ids)])
        production_orders.unlink()
    

    # Método para poner la fecha del pago a hoy
    def btn_setDate(self):
        # Fijar el campo date a la fecha de hoy
        today_date = fields.Date.today()
        self.write({'date': today_date})
