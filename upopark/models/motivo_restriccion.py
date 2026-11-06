# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MotivoRestriccion(models.Model):
    _name = 'upopark.motivo_restriccion'
    _description = 'Motivo de Restriccion'

    #atributos simples
    name = fields.Selection(
        [('impago', 'Impago'),
            ('sancion', 'Sancion'),
            ('no_autorizado', 'Vehículo no autorizado'),
            ('mantenimiento', 'Mantenimiento'),
            ('otro', 'Otro motivo')], string='Motivo de Restriccion', required=True)
    cDescripcion = fields.Text(string='Descripcion')

    #atributos complejos
    restriccion_ids = fields.One2many('upopark.restriccion_acceso','motivo_restriccion_id','Restricciones Aplicadas')

    #sql constraints
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'El motivo de restriccion ya esta registrado.')
    ]
