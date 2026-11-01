# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ColorVehiculo(models.Model):
    _name = 'upopark.color_vehiculo'
    _description = 'Color del Vehiculo'

    #atributos simples
    name = fields.Selection(
        [('blanco', 'Blanco'),
            ('negro', 'Negro'),
            ('gris', 'Gris'),
            ('azul', 'Azul'),
            ('rojo', 'Rojo'),
            ('verde', 'Verde'),
            ('amarillo', 'Amarillo'),
            ('otro', 'Otro')], string='Color Vehiculo', required=True)
    cDescripcion = fields.Text(string='Descripcion')

    #atributos complejos
    vehiculo_ids = fields.One2many('upopark.vehiculo','color_vehiculo_id','Vehiculos Registrados')