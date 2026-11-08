# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NivelAcceso(models.Model):
    
    _name = 'upoPark.nivelAcceso'
    _description = 'Grado de acceso requerido para entrar en una zona'
            
    nivelAcceso_zona = fields.One2many('upoPark.zona', 'NivelAcceso da acceso a Zona')
