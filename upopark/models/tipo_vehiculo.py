from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TipoVehiculo(models.Model):
    _name = 'upopark.tipo_vehiculo'
    _description = 'Tipo de Vehiculo'

    name = fields.Selection(
        [('coche', 'Coche'), ('moto', 'Moto'), ('furgoneta', 'Furgoneta'),
         ('camion', 'Camion'), ('autobus', 'Autobus')],
        string='Tipo de Vehiculo', required=True)
    descripcion = fields.Text(string='Descripcion')

    vehiculo_ids = fields.One2many('upopark.vehiculo', 'tipo_vehiculo_id', string='Vehiculos Registrados')

    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'El tipo de vehículo ya está registrado.')]

    @api.constrains('descripcion')
    def _check_longitud_descripcion_tipo(self):
        for record in self:
            if record.descripcion and not 5 <= len(record.descripcion) <= 250:
                raise ValidationError('La descripción del tipo de vehículo debe tener entre 5 y 250 caracteres.')