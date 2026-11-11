from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CancelacionReserva(models.Model):
    _name = 'upopark.cancelacion_reserva'
    _description = 'Cancelación de Reserva'

    fecha_cancelacion = fields.Datetime(string='Fecha de Cancelación', required=True)
    nota = fields.Text(string='Nota', help='Observaciones sobre el motivo de la cancelación.')

    reserva_id = fields.Many2one('upopark.reserva', string='Referencia Reserva', required=True)
    usuario_id = fields.Many2one('upopark.usuario', string='Usuario', required=True)

    _sql_constraints = [('reserva_uniq', 'UNIQUE(reserva_id)', 'Esta reserva ya ha sido cancelada.')]

    @api.onchange('fecha_cancelacion')
    def _onchange_fecha_cancelacion(self):
        if self.fecha_cancelacion and self.fecha_cancelacion > fields.Datetime.now():
            self.fecha_cancelacion = fields.Datetime.now()
            raise ValidationError('No puedes registrar una cancelación en el futuro.')

    @api.constrains('nota')
    def _check_nota_cancelacion(self):
        for record in self:
            if not record.nota or len(record.nota.strip()) < 10:
                raise ValidationError('La nota debe tener al menos 10 caracteres.')