# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TipoPlaza(models.Model):
    
    _name = 'upoPark.tipoPlaza'
    _description = 'Tipo de plaza'
        
    requiere_vehiculo_electrico = fields.Boolean(
            string='¿Requiere vehículo eléctrico?',
            default=False
        )

    accesible = fields.Boolean(
            string='¿Es una plaza accesible para discapacitados?',
            default=False
        )
        
    tipoPlaza_plaza = fields.Many2one('upoPark.plaza', 'TipoPlaza define Plaza')
    tipoPlaza_organizacion = fields.One2one('upoPark.organizacion', 'TipoPlaza pertenece a Organizacion')
