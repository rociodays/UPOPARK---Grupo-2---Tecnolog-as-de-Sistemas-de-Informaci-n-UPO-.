from odoo import models, fields, api

class SensorOcupacion(models.Model):
    _name = 'upopark.sensor_ocupacion'
    _description = 'Sensores de Ocupación'

    cod_ext = fields.Char(string='Código Externo', required=True)
    ult_conex = fields.Datetime(string='Última Conexión')
    
    estado_sensor_id = fields.Many2one('upopark.estado_sensor', string='Estado')
    estancia_id = fields.Many2one('upoPark.estancia', string='Estancia')