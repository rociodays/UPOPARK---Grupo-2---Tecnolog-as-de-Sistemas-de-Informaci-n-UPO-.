# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MotivoBloqueo(models.Model):
    
    _name = 'upoPark.motivoBloqueo'
    _description = 'Motivo de bloqueo de una plaza'

    motivo = fields.Char('Motivo', size=60, required=True)
    descripcion = fields.Char('Descripcion', size=60, required=True)

    motivoBloqueo_bloqueoPlaza = fields.One2one('upoPark.bloqueoPlaza', 'MotivoBloqueo resulta en BloqueoPlaza')
