# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Zona(models.Model):
    
    _name = 'upoPark.zona'
    _description = 'Una de las zonas en que se divide la universidad'
    
    nombre = fields.Char(string="Nombre Zona", size=60, required=True, help="El nombre del zona")
    codigo = fields.Char('Código', size=9, required=True)
        
    zona_nivelAcceso = fields.Many2one('upoPark.nivelAcceso', 'Zona requiere NivelAcceso')
    zona_aparcamiento = fields.One2many('upoPark.aparcamiento', 'Zona posee Aparcamientos')
