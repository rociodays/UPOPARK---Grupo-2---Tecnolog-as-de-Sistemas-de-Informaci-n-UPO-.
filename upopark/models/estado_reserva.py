from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EstadoReserva(models.Model):
    _name = 'upopark.estado_reserva'
    _description = 'Estados de Reserva'

    name = fields.Selection(
        [('borrador', 'Borrador'), ('confirmada', 'Confirmada'), ('activa', 'Activa'),
         ('finalizada', 'Finalizada'), ('cancelada', 'Cancelada')],
        string='Estado Reserva', required=True)
    descripcion = fields.Text(string='Descripcion')

    reserva_ids = fields.One2many('upopark.reserva', 'estado_reserva_id', string='Reservas en este Estado')

    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'El estado de reserva ya esta registrado.')]

    @api.constrains('descripcion')
    def _check_longitud_descripcion_estado(self):
        for record in self:
            if record.descripcion and not 5 <= len(record.descripcion) <= 250:
                raise ValidationError('La descripción del estado debe tener entre 5 y 250 caracteres.')