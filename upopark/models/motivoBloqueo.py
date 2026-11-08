# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MotivoBloqueo(models.Model):
    
    _name = 'upoPark.motivoBloqueo'
    _description = 'Motivo de bloqueo de una plaza'

    motivoBloqueo_bloqueoPlaza = fields.One2one('upoPark.bloqueoPlaza', 'MotivoBloqueo resulta en BloqueoPlaza')
