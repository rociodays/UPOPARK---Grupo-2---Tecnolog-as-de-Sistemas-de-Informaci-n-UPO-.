# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MaterialPavimento(models.Model):
    
    _name = 'upoPark.materialPavimento'
    _description = 'Material de pavimento del que está hecho un aparcamiento'

    materialPavimento_aparcamiento = fields.One2many('upoPark.aparcamiento', 'MaterialPavimento es suelo de Aparcamiento')
