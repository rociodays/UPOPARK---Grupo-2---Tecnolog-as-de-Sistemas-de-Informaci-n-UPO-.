# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadoConservacionPlaza(models.Model):
    
    _name = 'upoPark.estadoConservacionPlaza'
    _description = 'Estado de conservacion de una plaza'

    estado = fields.Char('Estado', size=9, required=True)
    activo = fields.Boolean(
            string='¿Estado activo?',
            default=True
        )
        
    estadoPlaza_plaza = fields.One2many('upoPark.plaza', 'EstadoPlaza muestra condicion de Plaza')
    estadoPlaza_indisponibilidad = fields.One2one('upoPark.indisponibilidad', 'EstadoPlaza puede generar Indisponibilidad')
    estadoPlaza_incidencia = fields.One2one('upoPark.incidencia', 'EstadoPlaza puede generar Incidencia')
