# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MotivoRestriccion(models.Model):
    _name = 'upopark.motivo_restriccion'
    _description = 'Motivo de Restriccion'

    name = fields.Selection(
        [('impago', 'Impago'),
            ('sancion', 'Sancion'),
            ('no_autorizado', 'Vehículo no autorizado'),
            ('mantenimiento', 'Mantenimiento'),
            ('otro', 'Otro motivo')], string='Motivo de Restriccion', required=True)
    cDescripcion = fields.Text(string='Descripcion')
