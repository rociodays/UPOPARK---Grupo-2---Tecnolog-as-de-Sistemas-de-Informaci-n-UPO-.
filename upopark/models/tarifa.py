from odoo import models, fields, api
class Tarifa(models.Model):
    _name = 'upopark.tarifa'
    _description = 'Tarifa de Precios'

    name = fields.Char(string='Nombre Tarifa', required=True)
    precio_kw = fields.Float(string='Precio por kW (€)', required=True)
    precio_minuto = fields.Float(string='Precio por Minuto (€)', required=True)

    linea_cargo_ids = fields.One2many('upopark.linea_cargo', 'tarifa_id', string='Cargos Aplicados')