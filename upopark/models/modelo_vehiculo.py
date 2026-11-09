from odoo import models, field, api

class ModeloVehiculo(models.Model):
    _name = 'upopark.modelo_vehiculo'
    _description = 'Modelo de vehiculo'

    nombre_modelo = fields.Char(string='Nombre del modelo', required=True)
    descripcion = fields.Char(string='Descripcion')

    vehiculo_id = fields.Many2one('upopark.vehiculo', string='Vehiculo', required=True)