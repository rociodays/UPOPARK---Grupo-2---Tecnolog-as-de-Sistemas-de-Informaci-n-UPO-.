# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TipoPlaza(models.Model):
    
    _name = 'upopark.tipo_plaza'
    _description = 'Tipo de plaza'
        
    codigo = fields.Char('Código', size=9, required=True)
    nombre = fields.Char('Nombre', size=9, required=True)

    requiere_vehiculo_electrico = fields.Boolean(
            string='¿Requiere vehículo eléctrico?',
            default=False
        )

    accesible = fields.Boolean(
            string='¿Es una plaza accesible para discapacitados?',
            default=False
        )
        
    tipo_plaza_plaza = fields.Many2one('upopark.plaza', 'TipoPlaza define Plaza')
    tipo_plaza_organizacion = fields.Many2one('upopark.organizacion', 'TipoPlaza pertenece a Organizacion')
