# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NivelAcceso(models.Model):
    
    _name = 'upoPark.nivelAcceso'
    _description = 'Grado de acceso requerido para entrar en una zona'
            
    nivel = fields.Integer('Material', size=2, required=True)
    descripcion = fields.Char('Descripcion', size=60, required=True)

    nivelAcceso_zona = fields.One2many('upoPark.zona', 'NivelAcceso da acceso a Zona')
