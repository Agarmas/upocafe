from odoo import api, models, fields

class Payment(models.Model):
    _name = 'upocafe.payment'
    _description = 'Pago de un conjunto de productos'

    date = fields.Date(string='Fecha')
    amount = fields.Float(string='Precio', compute='_compute_amount', store=True)
    payment_method_id = fields.Many2one('upocafe.payment_method', string='Metodo de pago')
    partner_id = fields.Many2one('res.partner', string='Cliente')
    currency_id = fields.Many2one('res.currency', string='Moneda')
    cancelation_id = fields.Many2one('upocafe.cancelation', string='Cancelacion')
    production_ids = fields.Many2many('mrp.production', string='Ordenes de producción')
    machine_id = fields.Many2one('upocafe.machine', string='Máquina')

    @api.depends('production_ids.product_qty', 'production_ids.product_id.lst_price')
    def _compute_amount(self):
        for record in self:
            record.amount = sum( (production.product_qty * production.product_id.lst_price) for production in record.production_ids)

    def btn_removeProductions(self):
        # Borramos los productos de este pago
        self.write({'production_ids':[(5,)]})


        # Borramos las ordenes de producción para no tener ordenes de producción invalidas
        production_orders = self.env['mrp.production'].search([('id', 'in', self.production_ids.ids)])
        production_orders.unlink()

        # Recargo la vista para que se vea reflejado
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
    
    def btn_setDate(self):
        # Fijar el campo date a la fecha de hoy
        today_date = fields.Date.today()
        self.write({'date': today_date})
        
        return {
            'type': 'ir.actions.client',
            'tag': 'reload', 
        }
