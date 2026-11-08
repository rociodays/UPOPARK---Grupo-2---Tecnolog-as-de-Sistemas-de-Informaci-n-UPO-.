# -*- coding: utf-8 -*-
from odoo import models, fields


class TipoInfraccion(models.Model):
    _name = 'upopark.tipo_infraccion'
    _description = 'Tipo de Infracción'
    _rec_name = 'sgravedad'

    sgravedad = fields.Char(string='Gravedad', required=True)
    fimporte_sugerido = fields.Float(string='Importe Sugerido')
