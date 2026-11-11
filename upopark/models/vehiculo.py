# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re

class Vehiculo(models.Model):
    _name = 'upopark.vehiculo'
    _description = 'Vehiculo'

    #atributos simples
    name = fields.Char(string="Matricula", required=True, help="Dame la matricula del vehiculo.")
    cPaisMatricula = fields.Char(string="Pais Matricula", required=True,help="Dame el pais de la matricula del vehiculo.")
    iNumeroPuertas = fields.Integer(string="Numero de Puertas", help="Número de puertas del vehiculo.")
    bTieneRemolque = fields.Boolean(string="Tiene Remolque", help="Indica si el vehiculo tiene remolque.")

    #atributos complejos
    color_vehiculo_id = fields.Many2one('upopark.color_vehiculo',string='Color', help="Dame el color del vehiculo.")
    tipo_vehiculo_id = fields.Many2one('upopark.tipo_vehiculo',string='Tipo de Vehículo',required=True, help="Dame el tipo de vehiculo.")
    modelo_vehiculo_id = fields.Many2one('upopark.modelo_vehiculo', string='Modelo', help='Dame el modelo del vehiculo.')
    etiqueta_medioambiental_id = fields.Many2one('upopark.etiqueta_medioambiental', string='Etiqueta Medioambiental', help='Dame la etiqueta medioambiental del vehiculo.')
    tipo_combustible_id = fields.Many2one('upopark.tipo_combustible', string='Tipo de Combustible', required=True, help='Dame el tipo de combustible.')
    contacto_id = fields.Many2one('upopark.contacto', string='Contacto', required=True, help='Dame el contacto propietario del vehiculo.')
    marca_vehiculo_id = fields.Many2one('upopark.marca_vehiculo', string='Marca', help='Dame la marca del vehiculo.')

    conector_ids = fields.Many2many('upopark.conector', string='Conectores Compatibles', help='Dame los conectores compatibles con el vehiculo.')

    restriccion_ids = fields.One2many('upopark.restriccion_acceso','vehiculo_id','Historial de Restricciones')
    reserva_ids = fields.One2many('upopark.reserva','vehiculo_id','Historial de Reservas')
    infraccion_ids = fields.One2many('upopark.infraccion', 'vehiculo_id','Historial de Infracciones')

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

    #uso de conectores solo para vehiculos electricos
    @api.onchange('tipo_combustible_id', 'conector_ids')
    def _onchange_combustible_conectores(self):
       if self.tipo_combustible_id and self.conector_ids:
           if self.tipo_combustible_id.name != 'Electrico':
               raise models.ValidationError('Solo los vehiculos electricos pueden tener conectores asignados.')

