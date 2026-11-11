from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class EventoCampus(models.Model):
    _name = 'upopark.evento_campus'
    _description = 'Evento Campus'

    nombre = fields.Char(string='Nombre', required=True)
    fecha_inicio = fields.Datetime(string='Fecha Inicio', required=True)
    fecha_fin = fields.Datetime(string='Fecha Fin', required=True)

    calendario_id = fields.Many2one('upopark.calendario', string='Calendario')

    @api.onchange('fecha_inicio')
    def _onchange_fecha_inicio(self):
        if self.fecha_inicio:
            self.fecha_fin = self.fecha_inicio + timedelta(hours=2)

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin and record.fecha_fin <= record.fecha_inicio:
                raise ValidationError('La fecha de fin debe ser posterior a la fecha de inicio del evento.')