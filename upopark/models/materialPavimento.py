# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MaterialPavimento(models.Model):
    
    _name = 'upoPark.materialPavimento'
    _description = 'Material de pavimento del que está hecho un aparcamiento'

    material = fields.Char('Material', size=60, required=True)
    descripcion = fields.Char('Estado', size=60, required=True)

    materialPavimento_aparcamiento = fields.One2many('upoPark.aparcamiento', 'MaterialPavimento es suelo de Aparcamiento')
