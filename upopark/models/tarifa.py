from odoo import models, fields

class Tarifa(models.Model):
    _name = 'upopark.tarifa'
    _description = 'Tarifa de Precios'

    name = fields.Char(string='Nombre Tarifa', required=True)
    precio_kw = fields.Float(string='Precio por kW (€)', required=True)
    precio_minuto = fields.Float(string='Precio por Minuto (€)', required=True)

    moneda_id = fields.Many2one('upopark.moneda', string='Moneda')
    tipo_servicio_tarifa_id = fields.Many2one('upopark.tipo_servicio_tarifa', string='Tipo de servicio')

    linea_cargo_ids = fields.One2many('upopark.linea_cargo', 'tarifa_id', string='Cargos Aplicados')