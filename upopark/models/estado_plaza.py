# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadoPlaza(models.Model):
    
    _name = 'upoPark.estado_plaza'
    _description = 'Estado de una plaza'

    estado = fields.Char('Estado', size=9, required=True)

    estadoPlaza_plaza = fields.One2one('upoPark.plaza', 'EstadoPlaza muestra estado de Plaza')
