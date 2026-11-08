# -*- coding: utf-8 -*-
from odoo import models, fields


class Festivo(models.Model):
    _name = 'upopark.festivo'
    _description = 'Festivo'
    _rec_name = 'snombre'

    snombre = fields.Char(string='Nombre', required=True)
    dfecha = fields.Date(string='Fecha', required=True)
