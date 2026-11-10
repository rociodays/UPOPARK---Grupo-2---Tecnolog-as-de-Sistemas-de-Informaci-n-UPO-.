# -*- coding: utf-8 -*-

from odoo import models, fields

class PoliticaReserva(models.Model):
    _name = 'upopark.politica_reserva'
    _description = 'Politica de Reserva'

    name = fields.Char(string='Codigo', required=True, help='Dame el codigo de la politica.')
    cNombre = fields.Char(string='Nombre', required=True, help='Dame el nombre de la politica.')
    iDiasAntelacion = fields.Integer(string='Dias de Antelacion', required=True, help='Dame el numero de dias de antelacion.')
    iDuracionMaxima = fields.Integer(string='Duracion Maxima', required=True, help='Dame la duracion maxima permitida.')
    iAntelacionCancel = fields.Integer(string='Antelacion Cancelacion', required=True, help='Dame los minutos de antelacion para cancelar la reserva.')