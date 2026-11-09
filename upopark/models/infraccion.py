from odoo import models, fields, api

class Infraccion(models.Model):
    _name = 'upopark.infraccion'
    _description = 'Infraccion'

    fecha = models.DateTime(string='Fecha', required=True)
    descripcion = fields.Char(string='Descripcion')
    importe = fields.Monetary(string='Importe', required=True)

    tipo_infraccion_id = fields.One2many('upopark.tipo_infraccion', string='Tipo de Infraccion')
    aparcamiento_id = fields.One2many('upopark.aparcamiento', string='Aparcamiento')
    vehiculo_id = fields.One2many('upopark.vehiculo', string='Vehiculo')
    alegacion_id = fields.Many2one('upopark.alegacion', string='Alegacion', required=True)