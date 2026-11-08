# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HistorialReserva(models.Model):
    _name = 'upopark.historial_reserva'
    _description = 'Historial de Cambios de Reserva'

    name = fields.Many2one('upopark.reserva', string='Reserva', required=True,help='Dame la reserva a la que pertenece este historial.')
    fFechaCambio = fields.Datetime('Fecha de Cambio', required=True, autodate = True, help="Dame la fecha de cambio de la reserva.")

    cNota = fields.Text(string='Nota', help='Observaciones sobre el motivo del cambio de estado.')
    
    estado_anterior_id = fields.Many2one('upopark.estado_reserva',string='Estado Anterior',required=True,help='Dame el estado anterior de la reserva.')
    estado_nuevo_id = fields.Many2one('upopark.estado_reserva',string='Estado Nuevo',required=True,help='Dame el estado nuevo de la reserva.')

    #sql constraints no tiene

    #validaciones
    #fecha cambio
    @api.onchange('fFechaCambio')
    def _onchange_fecha_cambio(self):
        resultado = {}
        if self.fFechaCambio:
            ahora = fields.Datetime.now()
            if self.fFechaCambio > ahora:
                self.fFechaCambio = ahora
                resultado = {
                    'warning': {
                        'title': 'Fecha de historial invalida',
                        'message': 'El registro historico no puede estar en el futuro.'
                    }
                }
                return resultado

    #estados
    @api.constrains('estado_anterior_id', 'estado_nuevo_id')
    def _check_cambio_estado_real(self):
        for record in self:
            if record.estado_anterior_id and record.estado_nuevo_id:
                if record.estado_anterior_id.id == record.estado_nuevo_id.id:
                    raise ValidationError('Operacion rechazada: El estado nuevo debe ser diferente al estado anterior.')