from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MotivoRestriccion(models.Model):
    _name = 'upopark.motivo_restriccion'
    _description = 'Motivo de Restriccion'

    name = fields.Selection(
        [('impago', 'Impago'), ('sancion', 'Sancion'),
         ('no_autorizado', 'Vehículo no autorizado'),
         ('mantenimiento', 'Mantenimiento'), ('otro', 'Otro motivo')],
        string='Motivo de Restriccion', required=True)
    descripcion = fields.Text(string='Descripcion')

    restriccion_ids = fields.One2many(
        'upopark.restriccion_acceso', 'motivo_restriccion_id', string='Restricciones Aplicadas')

    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'El motivo de restriccion ya esta registrado.')]

    @api.constrains('descripcion')
    def _check_longitud_descripcion_motivo(self):
        for record in self:
            if record.descripcion and not 5 <= len(record.descripcion) <= 250:
                raise ValidationError('La descripción del motivo debe tener entre 5 y 250 caracteres.')