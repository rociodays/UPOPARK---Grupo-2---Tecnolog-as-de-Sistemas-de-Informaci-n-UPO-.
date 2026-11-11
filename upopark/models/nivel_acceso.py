# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NivelAcceso(models.Model):
    
    _name = 'upopark.nivel_acceso'
    _description = 'Grado de acceso requerido para entrar en una zona'
            
    nivel = fields.Integer('Material', size=2, required=True)
    descripcion = fields.Char('Descripcion', size=60, required=True)

    nivel_acceso_zona = fields.One2many('upopark.zona', 'NivelAcceso da acceso a Zona')
