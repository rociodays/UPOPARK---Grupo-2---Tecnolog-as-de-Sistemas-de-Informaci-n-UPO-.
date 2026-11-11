from odoo import models, fields, api

class MarcaVehiculo(models.Model):
    _name = 'upopark.marca_vehiculo'
    _description = 'Marca de Vehículo'

    name = fields.Char(string='Nombre de la Marca', required=True)
    pais_origen = fields.Char(string='País de Origen')
    vehiculo_ids = fields.One2many('upopark.vehiculo', 'marca_id', string='Vehículos')