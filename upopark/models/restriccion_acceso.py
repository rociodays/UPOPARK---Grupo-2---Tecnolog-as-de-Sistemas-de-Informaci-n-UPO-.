from odoo import models, fields, api
from odoo.exceptions import ValidationError


class RestriccionAcceso(models.Model):
    _name = 'upopark.restriccion_acceso'
    _description = 'Restriccion de Acceso'

    name = fields.Char(string='Matrícula', required=True)
    fecha_inicio = fields.Datetime(string='Inicio', required=True)
    fecha_fin = fields.Datetime(string='Fin', required=True)
    activo = fields.Boolean(string='Activa', compute='_compute_activo')

    vehiculo_id = fields.Many2one('upopark.vehiculo', string='Vehículo', required=True)
    motivo_restriccion_id = fields.Many2one('upopark.motivo_restriccion', string='Motivo', required=True)

    @api.depends('fecha_inicio', 'fecha_fin')
    def _compute_activo(self):
        ahora = fields.Datetime.now()
        for record in self:
            record.activo = bool(
                record.fecha_inicio and record.fecha_fin
                and record.fecha_inicio <= ahora <= record.fecha_fin
            )

    @api.onchange('fecha_inicio')
    def _onchange_fecha_inicio(self):
        if self.fecha_inicio and self.fecha_inicio < fields.Datetime.now():
            self.fecha_inicio = fields.Datetime.now()
            raise ValidationError('La restricción no puede empezar en el pasado.')

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_rango_fechas(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin and record.fecha_fin < record.fecha_inicio:
                raise ValidationError('La fecha de fin no puede ser anterior a la de inicio.')