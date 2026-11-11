# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Zona(models.Model):
    
    _name = 'upopark.zona'
    _description = 'Una de las zonas en que se divide la universidad'
    
    nombre = fields.Char(string="Nombre Zona", size=60, required=True, help="El nombre del zona")
    codigo = fields.Char('Código', size=9, required=True)
        
    zona_nivel_acceso = fields.Many2one('upopark.nivel_acceso', 'Zona requiere NivelAcceso')
    zona_aparcamiento = fields.One2many('upopark.aparcamiento', 'Zona posee Aparcamientos')
