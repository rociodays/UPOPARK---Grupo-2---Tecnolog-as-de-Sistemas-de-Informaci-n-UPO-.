# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vehiculo(models.Model):
     _name = 'upopark.vehiculo'
     _description = 'Vehiculo'

     name = fields.Char(string="Matricula", required=True, help="Dame la matrícula del vehiculo.")
     cPaisMatricula = fields.Char(string="Pais Matricula", required=True,help="Dame el pais de la matrícula del vehiculo.")
     iNumeroPuertas = fields.Integer(string="Numero de Puertas", help="Número de puertas del vehículo.")
     bTieneRemolque = fields.Boolean(string="Tiene Remolque", default=False, help="Indica si el vehículo tiene remolque.")


