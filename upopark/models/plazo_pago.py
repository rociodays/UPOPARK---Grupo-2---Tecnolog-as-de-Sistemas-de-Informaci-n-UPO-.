from odoo import models, fields

class PlazoPago(models.Model):
    _name = 'upopark.plazo_pago'
    _description = 'Plazo de Pago'
    _rec_name = 'categoria'

    categoria = fields.Char(string='Categoría', required=True)
    dias = fields.Integer(string='Días')