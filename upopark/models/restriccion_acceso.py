# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RestriccionAcceso(models.Model):
    _name = 'upopark.restriccion_acceso'
    _description = 'Restriccion de Acceso'

    name = fields.Char(string="Matricula", required=True, help="Dame la matrícula del vehiculo.")
    fInicio = fields.Datetime('Inicio', required=True, autodate = True, help="Dame la fecha de inicio de la restriccion.")
    fFin = fields.Datetime('Fin', required=True, autodate = True, help="Dame la fecha de fin de la restriccion.")


