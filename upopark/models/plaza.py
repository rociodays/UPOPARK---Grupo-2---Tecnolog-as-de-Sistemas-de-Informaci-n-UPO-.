# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Plaza(models.Model):
    
    _name = 'upoPark.plaza'
    _description = 'Una de las plazas existentes'
    
    codigo = fields.Char('Código', size=9, required=True)
    longitud = fields.Integer("Longitud en metros")
    anchura = fields.Integer("Anchura en metros")
        
    plaza_bloqueoPlaza = fields.Many2one('upoPark.bloqueoPlaza', 'Plaza puede verse afectada por BloqueoPlaza')
    plaza_aparcamiento = fields.Many2one('upoPark.aparcamiento', 'Plaza pertenece a Aparcamiento')
    plaza_estadoPlaza = fields.One2one('upoPark.estadoPlaza', 'Plaza está en un EstadoPlaza')
    plaza_conector = fields.One2one('upoPark.conector', 'Plaza puede tener un Conector')
    plaza_sensorOcupacion = fields.One2one('upoPark.sensorOcupacion', 'Plaza puede tener un SensorOcupacion')
