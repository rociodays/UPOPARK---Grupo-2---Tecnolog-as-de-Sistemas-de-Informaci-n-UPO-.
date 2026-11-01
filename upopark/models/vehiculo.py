# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vehiculo(models.Model):
     _name = 'upopark.vehiculo'
     _description = 'Vehiculo'

     #atributos simples
     name = fields.Char(string="Matricula", required=True, help="Dame la matrícula del vehiculo.")
     cPaisMatricula = fields.Char(string="Pais Matricula", required=True,help="Dame el pais de la matrícula del vehiculo.")
     iNumeroPuertas = fields.Integer(string="Numero de Puertas", help="Número de puertas del vehículo.")
     bTieneRemolque = fields.Boolean(string="Tiene Remolque", default=False, help="Indica si el vehículo tiene remolque.")

     #atributos complejos
     color_vehiculo_id = fields.Many2one('upopark.color_vehiculo',string='Color', help="Dame el color del vehiculo.")
     tipo_vehiculo_id = fields.Many2one('upopark.tipo_vehiculo',string='Tipo de Vehículo',required=True, help="Dame el tipo de vehiculo.")
