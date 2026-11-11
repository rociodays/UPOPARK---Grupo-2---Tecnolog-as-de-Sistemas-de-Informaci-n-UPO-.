from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HistorialReserva(models.Model):
    _name = 'upopark.historial_reserva'
    _description = 'Historial de Cambios de Reserva'

    fecha_cambio = fields.Datetime(string='Fecha de Cambio', required=True)
    nota = fields.Text(string='Nota', help='Observaciones sobre el motivo del cambio de estado.')

    reserva_id = fields.Many2one('upopark.reserva', string='Reserva', required=True)
    estado_anterior_id = fields.Many2one('upopark.estado_reserva', string='Estado Anterior', required=True)
    estado_nuevo_id = fields.Many2one('upopark.estado_reserva', string='Estado Nuevo', required=True)

    @api.onchange('fecha_cambio')
    def _onchange_fecha_cambio(self):
        if self.fecha_cambio and self.fecha_cambio > fields.Datetime.now():
            self.fecha_cambio = fields.Datetime.now()
            raise ValidationError('El registro histórico no puede estar en el futuro.')

    @api.constrains('estado_anterior_id', 'estado_nuevo_id')
    def _check_cambio_estado_real(self):
        for record in self:
            if record.estado_anterior_id and record.estado_nuevo_id and record.estado_anterior_id.id == record.estado_nuevo_id.id:
                raise ValidationError('El estado nuevo debe ser diferente al estado anterior.')