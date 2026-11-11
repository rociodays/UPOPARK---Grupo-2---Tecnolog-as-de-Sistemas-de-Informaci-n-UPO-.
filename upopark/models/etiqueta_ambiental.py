from odoo import models, fields, api

class EtiquetaAmbiental(models.Model):
    _name = 'upopark.etiqueta_ambiental'
    _description = 'Etiqueta Ambiental'

    name = fields.Char(string='Código DGT', required=True)
    descripcion = fields.Text(string='Descripción')
    color_distintivo = fields.Char(string='Color Distintivo')
    vehiculo_ids = fields.One2many('upopark.vehiculo', 'etiqueta_ambiental_id', string='Vehículos')