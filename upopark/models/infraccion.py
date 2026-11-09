from odoo import models, fields, api

class Infraccion(models.Model):
    _name = 'upopark.infraccion'
    _description = 'Infraccion'

    fecha = models.DateTime(string='Fecha', required=True)
    descripcion = fields.Char(string='Descripcion')
    importe = fields.Monetary(string='Importe', required=True)

    tipo_infraccion_id = fields.Many2one('upopark.tipo_infraccion', string='Tipo de Infraccion', required=True)
    aparcamiento_id = fields.Many2one('upopark.aparcamiento', string='Aparcamiento', required=True)
    vehiculo_id = fields.Many2one('upopark.vehiculo', string='Vehiculo', required=True)
    alegacion_id = fields.Many2one('upopark.alegacion', string='Alegacion', required=True)
    sancion_id = fields.Many2one('upopark.sancion', string='Sancion')