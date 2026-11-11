# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MotivoBloqueo(models.Model):
    
    _name = 'upopark.motivo_bloqueo'
    _description = 'Motivo de bloqueo de una plaza'

    motivo = fields.Char('Motivo', size=60, required=True)
    descripcion = fields.Char('Descripcion', size=60, required=True)

    motivo_bloqueo_bloqueo_plaza = fields.Many2one('upopark.bloqueo_plaza', 'MotivoBloqueo resulta en BloqueoPlaza')
