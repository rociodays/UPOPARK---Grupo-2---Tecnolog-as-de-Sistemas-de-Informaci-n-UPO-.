# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reserva(models.Model):
    _name = 'upopark.reserva'
    _description = 'Reserva de Parking'

    name = fields.Char(string="Referencia", required=True, help="Dame la referencia de la reserva.")
    fInicio = fields.Datetime('Inicio', required=True, autodate = True, help="Dame la fecha de inicio de la reserva.")
    fFin = fields.Datetime('Fin', required=True, autodate = True, help="Dame la fecha de fin de la reserva.")


