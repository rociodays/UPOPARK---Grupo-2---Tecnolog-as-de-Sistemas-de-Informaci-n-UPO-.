from odoo import models, fields

class TipoServicioTarifa(models.Model):
    _name = 'upopark.tipo_servicio_tarifa'
    _description = 'Tipo de servicio de Tarifa'

    tipo = fields.Char(string='Tipo', required=True)
    descripcion = fields.Char(string='Descripción')

    tarifa_ids = fields.One2many('upopark.tarifa', 'tipo_servicio_tarifa_id', string='Tarifas')