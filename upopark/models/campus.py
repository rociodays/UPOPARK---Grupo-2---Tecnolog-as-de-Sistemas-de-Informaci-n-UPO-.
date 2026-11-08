# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Campus(models.Model):
    
    _name = 'upoPark.campus'
    _description = 'Campus Universitario'
    
    nombre = fields.Char(string="Nombre Campus", size=60, required=True, help="El nombre del campus")
    codigo = fields.Char('Código', size=9, required=True)
    direccion = fields.Char('Dirección', size=60, required=True)
    latitud = fields.Char('Latitud', size=9, required=True)
    longitud = fields.Char('Longitud', size=9, required=True)
    
    campus_organización = fields.Many2one('upoPark.organizacion', 'Campus pertenece a Organización')
    campus_aparcamiento = fields.One2many('upoPark.aparcamiento', 'Campus gestiona Aparcamiento')