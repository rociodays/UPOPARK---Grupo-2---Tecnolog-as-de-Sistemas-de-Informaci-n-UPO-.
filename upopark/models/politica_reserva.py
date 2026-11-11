from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PoliticaReserva(models.Model):
    _name = 'upopark.politica_reserva'
    _description = 'Politica de Reserva'

    name = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre')
    dias_antelacion = fields.Integer(string='Días de antelación', required=True)
    duracion_maxima = fields.Integer(string='Duración máxima (días)', required=True)
    antelacion_cancelacion = fields.Integer(string='Antelación de cancelación (min)', required=True)

    reserva_ids = fields.One2many('upopark.reserva', 'politica_reserva_id', string='Reservas vinculadas')

    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'El código de la política ya está registrado.')]

    @api.constrains('nombre')
    def _check_longitud_nombre(self):
        for record in self:
            if record.nombre and not 3 <= len(record.nombre) <= 100:
                raise ValidationError('El nombre de la política debe tener entre 3 y 100 caracteres.')

    @api.constrains('duracion_maxima', 'dias_antelacion', 'antelacion_cancelacion')
    def _check_valores_numericos(self):
        for record in self:
            if record.duracion_maxima < 1:
                raise ValidationError('La duración máxima debe ser al menos 1 día.')
            if record.dias_antelacion < 0:
                raise ValidationError('Los días de antelación no pueden ser negativos.')
            if record.antelacion_cancelacion < 0:
                raise ValidationError('La antelación de cancelación no puede ser negativa.')