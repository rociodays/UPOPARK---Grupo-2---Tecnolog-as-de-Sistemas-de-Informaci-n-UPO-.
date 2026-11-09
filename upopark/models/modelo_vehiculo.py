from odoo import models, fields, api

class ModeloVehiculo(models.Model):
    _name = 'upopark.modelo_vehiculo'
    _description = 'Modelo de vehiculo'

    nombre_modelo = fields.Char(string='Nombre del modelo', required=True)
    descripcion = fields.Char(string='Descripcion')

    vehiculo_ids = fields.One2many('upopark.vehiculo', 'modelo_vehiculo_id', string='Vehiculos')