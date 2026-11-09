from odoo import models, fields, api

class Infraccion(models.Model):
    _name = 'upopark.infraccion'
    _description = 'Infraccion'

    fecha = models.DateTime(string='Fecha', required=True)
    descripcion = fields.Char(string='Descripcion')
    importe = fields.Monetary(string='Importe', required=True)

    tipo_infraccion_id = fields.One2Many('upopark.tipo_infraccion', string='Tipo de Infraccion')
    aparcamiento_id = fields.One2Many('upopark.aparcamiento', string='Aparcamiento')
    vehiculo_id = fields.One2Many('upopark.vehiculo', string='Vehiculo')
    alegacion_id = fields.Many2one('upopark.alegacion', string='Alegacion', required=True)