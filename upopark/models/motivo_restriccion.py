# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

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

    #validaciones
    @api.constrains('cDescripcion')
    def _check_longitud_descripcion_motivo(self):
        for record in self:
            if record.cDescripcion:
                if len(record.cDescripcion) < 5 or len(record.cDescripcion) > 250:
                    raise ValidationError('La descripcion del motivo debe tener entre 5 y 250 caracteres.')