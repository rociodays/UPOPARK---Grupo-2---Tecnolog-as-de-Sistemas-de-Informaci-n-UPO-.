# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoVehiculo(models.Model):
    _name = 'upopark.tipo_vehiculo'
    _description = 'Tipo de Vehiculo'

    name = fields.Selection(
        [('coche', 'Coche'),
            ('moto', 'Moto'),
            ('furgoneta', 'Furgoneta'),
            ('camion', 'Camion'),
            ('autobus', 'Autobus')], string='Tipo de Vehículo', required=True)
    cDescription = fields.Text(string='Descripcion')
