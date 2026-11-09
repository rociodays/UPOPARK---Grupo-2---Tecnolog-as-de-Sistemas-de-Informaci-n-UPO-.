# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BloqueoPlaza(models.Model):
    
    _name = 'upoPark.bloqueoPlaza'
    _description = 'Situación de bloqueo de una plaza'

    referencia = fields.Char('Referencia', size=9, required=True)
    inicio = fields.Datetime('Comienzo', required=True, autodate = True)
    fin = fields.Datetime('Final', required=True, autodate = True)
    
    activo = fields.Boolean(
            string='¿Bloqueo en estado activo?',
            default=False
        )

    bloqueoPlaza_plaza = fields.One2one('upoPark.plaza', 'BloqueoPlaza afecta a Plaza')
    bloqueoPlaza_motivoBloqueo = fields.One2one('upoPark.motivoBloqueo', 'BloqueoPlaza se debe a MotivoBloqueo')
    bloqueoPlaza_incidencia = fields.One2one('upoPark.incidencia', 'BloqueoPlaza se debe a Incidencia')
