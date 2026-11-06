# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoVehiculo(models.Model):
    _name = 'upopark.tipo_vehiculo'
    _description = 'Tipo de Vehiculo'

    #atributos simples
    name = fields.Selection(
        [('coche', 'Coche'),
            ('moto', 'Moto'),
            ('furgoneta', 'Furgoneta'),
            ('camion', 'Camion'),
            ('autobus', 'Autobus')], string='Tipo de Vehiculo', required=True)
    cDescripcion = fields.Text(string='Descripcion')

    #atributos complejos
    vehiculo_ids = fields.One2many('upopark.vehiculo','tipo_vehiculo_id','Vehiculos Registrados')

    #sql constraints
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'El tipo de vehículo ya está registrado.')
    ]