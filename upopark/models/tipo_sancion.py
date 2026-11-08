# -*- coding: utf-8 -*-
from odoo import models, fields


class TipoSancion(models.Model):
    _name = 'upopark.tipo_sancion'
    _description = 'Tipo de Sanción'
    _rec_name = 'snombre'

    snombre = fields.Char(string='Nombre', required=True)
    sdescripcion = fields.Text(string='Descripción')
    sancion_ids = fields.One2many('upopark.sancion', 'tipo_sancion_id', string='Sanciones')
