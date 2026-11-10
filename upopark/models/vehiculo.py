# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re

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

    restriccion_ids = fields.One2many('upopark.restriccion_acceso','vehiculo_id','Historial de Restricciones')
    reserva_ids = fields.One2many('upopark.reserva','vehiculo_id','Historial de Reservas')

    #sql constraints
    _sql_constraints = [
       ('name_uniq', 'UNIQUE(name)', 'La matrícula del vehículo ya está registrada.')
    ]

    #validaciones
    #matricula formato
    @api.constrains('name')
    def _check_formato_matricula(self):
       for record in self:
           if record.name:
               if not re.match(r'^[A-Z0-9]{4,10}$', record.name):
                   raise models.ValidationError('El formato de la matricula es incorrecto.')

    #numero de puertas rango
    @api.onchange('iNumeroPuertas')
    def _onchange_rango_puertas(self):
       if self.iNumeroPuertas and (self.iNumeroPuertas < 0 or self.iNumeroPuertas > 5):
           raise models.ValidationError('Un vehiculo estandar no puede tener menos de 0 ni mas de 5 puertas.')

