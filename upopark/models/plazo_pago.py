# -*- coding: utf-8 -*-
from odoo import models, fields


class PlazoPago(models.Model):
    _name = 'upopark.plazo_pago'
    _description = 'Plazo de Pago'
    _rec_name = 'scategoria'

    scategoria = fields.Char(string='Categoría', required=True)
    idias = fields.Integer(string='Días')
