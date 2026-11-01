# -*- coding: utf-8 -*-

from odoo import models, fields

class HistorialReserva(models.Model):
    _name = 'upopark.historial_reserva'
    _description = 'Historial de Cambios de Reserva'

    name = fields.Many2one()

    cNota = fields.Text(string='Nota', help='Observaciones sobre el motivo del cambio de estado.')
    fFechaCambio = fields.Datetime('Fecha de Cambio', required=True, autodate = True, help="Dame la fecha de cambio de la reserva.")
    
    cEstadoNuevo = fields.Many2one()
    cEstadoNuevo = fields.Many2one()