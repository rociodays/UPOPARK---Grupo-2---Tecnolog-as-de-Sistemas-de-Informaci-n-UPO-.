# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RestriccionAcceso(models.Model):
    _name = 'upopark.restriccion_acceso'
    _description = 'Restriccion de Acceso'

    #atributos simples
    name = fields.Char(string="Matricula", required=True, help="Dame la matrícula del vehiculo.")
    fInicio = fields.Datetime('Inicio', required=True, autodate = True, help="Dame la fecha de inicio de la restriccion.")
    fFin = fields.Datetime('Fin', required=True, autodate = True, help="Dame la fecha de fin de la restriccion.")

    #atributos complejos
    vehiculo_id = fields.Many2one('upopark.vehiculo',string='Vehículo',required=True,help='Dame el vehículo al que se le aplica la restriccion.')
    motivo_restriccion_id = fields.Many2one('upopark.motivo_restriccion', string='Motivo de Restricción',required=True, help='Dame el motivo de la restriccion.')

    #sql constraints no tiene

    