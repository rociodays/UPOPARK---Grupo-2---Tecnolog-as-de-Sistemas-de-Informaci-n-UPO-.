from odoo import models, fields

class Plaza(models.Model):
    _name = 'upopark.plaza'
    _description = 'Una de las plazas existentes'

    codigo = fields.Char(string='Código', size=9, required=True)
    longitud = fields.Integer(string='Longitud en metros')
    anchura = fields.Integer(string='Anchura en metros')

    plaza_bloqueo_plaza = fields.Many2one('upopark.bloqueo_plaza', string='Bloqueo que la afecta')
    plaza_aparcamiento = fields.Many2one('upopark.aparcamiento', string='Aparcamiento')
    plaza_estado_plaza = fields.Many2one('upopark.estado_plaza', string='Estado de la plaza')
    plaza_conector = fields.Many2one('upopark.conector', string='Conector')
    plaza_sensor_ocupacion = fields.Many2one('upopark.sensor_ocupacion', string='Sensor de ocupación')
    plaza_estado_conservacion = fields.Many2one('upopark.estado_conservacion_plaza', string='Estado de conservación')
    tipo_plaza_id = fields.Many2one('upopark.tipo_plaza', string='Tipo de plaza')