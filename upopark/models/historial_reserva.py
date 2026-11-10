# -*- coding: utf-8 -*-

from odoo import models, fields

class HistorialReserva(models.Model):
    _name = 'upopark.historial_reserva'
    _description = 'Historial de Cambios de Reserva'

    name = fields.Many2one('upopark.reserva', string='Reserva', required=True,help='Dame la reserva a la que pertenece este historial.')

    cNota = fields.Text(string='Nota', help='Observaciones sobre el motivo del cambio de estado.')
    fFechaCambio = fields.Datetime('Fecha de Cambio', required=True, autodate = True, help="Dame la fecha de cambio de la reserva.")
    
    estado_anterior_id = fields.Many2one('upopark.estado_reserva',string='Estado Anterior',required=True,help='Dame el estado anterior de la reserva.')
    estado_nuevo_id = fields.Many2one('upopark.estado_reserva',string='Estado Nuevo',required=True,help='Dame el estado nuevo de la reserva.')