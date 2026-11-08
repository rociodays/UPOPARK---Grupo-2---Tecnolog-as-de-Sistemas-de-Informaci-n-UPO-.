from odoo import models, fields, api

class EstadoSensor(models.Model):
    _name = 'upopark.estado_sensor'
    _description = 'Estados del Sensor de Ocupación'

    nombre = fields.Char(string='Estado', required=True)
    descripcion = fields.Char(string='Descripción')
    
    sensor_ids = fields.One2many('upopark.sensor_ocupacion', 'estado_sensor_id', string='Sensores')
