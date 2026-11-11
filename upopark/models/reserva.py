from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Reserva(models.Model):
    _name = 'upopark.reserva'
    _description = 'Reserva de Parking'

    name = fields.Char(string='Referencia', required=True, help='Referencia de la reserva.')
    fecha_inicio = fields.Datetime(string='Inicio', required=True)
    fecha_fin = fields.Datetime(string='Fin', required=True)

    vehiculo_id = fields.Many2one('upopark.vehiculo', string='Vehículo', required=True)
    estado_reserva_id = fields.Many2one('upopark.estado_reserva', string='Estado Actual', required=True)
    politica_reserva_id = fields.Many2one('upopark.politica_reserva', string='Política Aplicada', required=True)
    contacto_id = fields.Many2one('upopark.contacto', string='Contacto', required=True)
    plaza_id = fields.Many2one('upopark.plaza', string='Plaza', required=True)

    historial_ids = fields.One2many('upopark.historial_reserva', 'reserva_id', string='Historial de Cambios')
    cancelacion_ids = fields.One2many('upopark.cancelacion_reserva', 'reserva_id', string='Registros de Cancelación')

    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'La referencia de la reserva ya está registrada.')]

    @api.constrains('name')
    def _check_formato_referencia(self):
        for record in self:
            if record.name and not re.match(r'^RES-\d{4}-\d{3,6}$', record.name):
                raise ValidationError('La referencia debe seguir el formato RES-YYYY-XXXX.')

    @api.onchange('fecha_inicio')
    def _onchange_fecha_inicio_reserva(self):
        if self.fecha_inicio:
            ahora = fields.Datetime.now()
            if self.fecha_inicio < ahora:
                self.fecha_inicio = ahora
                raise ValidationError('No puedes crear una reserva en el pasado.')

    @api.constrains('fecha_inicio', 'fecha_fin', 'politica_reserva_id')
    def _check_logica_fechas_y_politica(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin:
                if record.fecha_fin <= record.fecha_inicio:
                    raise ValidationError('La fecha de fin debe ser posterior a la de inicio.')
                if record.politica_reserva_id and record.politica_reserva_id.duracion_maxima:
                    diferencia = record.fecha_fin - record.fecha_inicio
                    if diferencia.days > record.politica_reserva_id.duracion_maxima:
                        raise ValidationError(
                            f'La reserva de {diferencia.days} días excede el límite de '
                            f'{record.politica_reserva_id.duracion_maxima} días.'
                        )

    @api.constrains('contacto_id', 'vehiculo_id')
    def _check_propietario_vehiculo(self):
        for record in self:
            if record.contacto_id and record.vehiculo_id and record.vehiculo_id.contacto_id.id != record.contacto_id.id:
                raise ValidationError('El contacto debe ser el propietario del vehículo.')