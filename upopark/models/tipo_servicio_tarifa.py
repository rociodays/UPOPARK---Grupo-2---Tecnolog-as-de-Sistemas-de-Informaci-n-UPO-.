from odoo import models, fields, api

class TipoServicioTarifa(models.Model):
    _name = 'upopark.tipo_servicio_tarifa'
    _description = 'Tipo de servicio de Tarifa'

    tipo = fields.Char(string='Tipo', required=True)
    descripcion = fields.Char(string='Descripcion')

    tarifa_ids = fields.One2Many('upopark.tarifa', 'tipo_servicio_tarifa_id', string='Tarifas')