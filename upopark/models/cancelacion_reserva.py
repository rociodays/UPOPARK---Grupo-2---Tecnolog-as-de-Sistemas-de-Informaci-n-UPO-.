from odoo import models, fields

class CancelacionReserva(models.Model):
    _name = 'upopark.cancelacion_reserva'
    _description = 'Cancelacion de Reserva'

    name = fields.Many2one()

    fFechaCancelacion = fields.Datetime('Fecha de Cancelacion', required=True, autodate = True, help="Dame la fecha de cancelacion de la reserva.")
    cNota = fields.Text(string='Nota', help='Observaciones sobre el motivo del cambio de estado.')