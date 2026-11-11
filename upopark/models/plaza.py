from odoo import models, fields, api

class Plaza(models.Model):
    
    _name = 'upopark.plaza'
    _description = 'Una de las plazas existentes'
    
    codigo = fields.Char('Código', size=9, required=True)
    longitud = fields.Integer("Longitud en metros")
    anchura = fields.Integer("Anchura en metros")
        
    plaza_bloqueo_plaza = fields.Many2one('upopark.bloqueo_plaza', 'Plaza puede verse afectada por BloqueoPlaza')
    plaza_aparcamiento = fields.Many2one('upopark.aparcamiento', 'Plaza pertenece a Aparcamiento')
    plaza_estadoPlaza = fields.Many2one('upopark.estadoPlaza', 'Plaza está en un EstadoPlaza')
    plaza_conector = fields.Many2one('upopark.conector', 'Plaza puede tener un Conector')
    plaza_sensorOcupacion = fields.Many2one('upopark.sensorOcupacion', 'Plaza puede tener un SensorOcupacion')
