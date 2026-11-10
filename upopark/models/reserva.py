# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reserva(models.Model):
    _name = 'upopark.reserva'
    _description = 'Reserva de Parking'

    #atributos simples
    name = fields.Char(string="Referencia", required=True, help="Dame la referencia de la reserva.")
    fInicio = fields.Datetime('Inicio', required=True, autodate = True, help="Dame la fecha de inicio de la reserva.")
    fFin = fields.Datetime('Fin', required=True, autodate = True, help="Dame la fecha de fin de la reserva.")

    #atributos complejos
    vehiculo_id = fields.Many2one('upopark.vehiculo',string='Vehículo',required=True,help='Dame el vehiculo para esta reserva.')
    estado_reserva_id = fields.Many2one('upopark.estado_reserva',string='Estado Actual',required=True,help='Dame el estado actual de la reserva.')
    politica_reserva_id = fields.Many2one('upopark.politica_reserva',string='Política Aplicada',required=True,help='Dame la politica aplicada a esta reserva.')
    
    historial_ids = fields.One2many('upopark.historial_reserva','reserva_id','Historial de Cambios')
    cancelacion_ids = fields.One2many('upopark.cancelacion_reserva','reserva_id','Registros de Cancelación')