from odoo import models, fields

class Infraccion(models.Model):
    _name = 'upopark.infraccion'
    _description = 'Infracción'

    fecha = fields.Datetime(string='Fecha', required=True)
    descripcion = fields.Char(string='Descripción')
    importe = fields.Monetary(string='Importe', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Moneda')

    tipo_infraccion_id = fields.Many2one('upopark.tipo_infraccion', string='Tipo de Infracción', required=True)
    aparcamiento_id = fields.Many2one('upopark.aparcamiento', string='Aparcamiento', required=True)
    vehiculo_id = fields.Many2one('upopark.vehiculo', string='Vehículo', required=True)
    alegacion_id = fields.Many2one('upopark.alegacion', string='Alegación')
    sancion_id = fields.Many2one('upopark.sancion', string='Sanción')