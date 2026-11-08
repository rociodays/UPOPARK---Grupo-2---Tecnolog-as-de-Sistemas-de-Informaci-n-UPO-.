from odoo import models, fields, api

class TipoCombustible(models.Model):
    _name = 'upopark.tipo_combustible'
    _description = 'Tipo de Combustible'

    name = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre', required=True)

    vehiculo_ids = fields.One2many('upopark.vehiculo', 'tipo_combustible_id', string='Vehículos')