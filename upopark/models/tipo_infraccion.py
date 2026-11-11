from odoo import models, fields

class TipoInfraccion(models.Model):
    _name = 'upopark.tipo_infraccion'
    _description = 'Tipo de Infracción'
    _rec_name = 'gravedad'

    gravedad = fields.Char(string='Gravedad', required=True)
    importe_sugerido = fields.Float(string='Importe Sugerido')