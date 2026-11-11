from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ColorVehiculo(models.Model):
    _name = 'upopark.color_vehiculo'
    _description = 'Color del Vehiculo'

    name = fields.Selection(
        [('blanco', 'Blanco'), ('negro', 'Negro'), ('gris', 'Gris'),
         ('azul', 'Azul'), ('rojo', 'Rojo'), ('verde', 'Verde'),
         ('amarillo', 'Amarillo'), ('otro', 'Otro')],
        string='Color Vehiculo', required=True)
    descripcion = fields.Text(string='Descripcion')

    vehiculo_ids = fields.One2many('upopark.vehiculo', 'color_vehiculo_id', string='Vehiculos Registrados')

    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'El color ya está registrado.')]

    @api.constrains('descripcion')
    def _check_longitud_descripcion_color(self):
        for record in self:
            if record.descripcion and not 5 <= len(record.descripcion) <= 250:
                raise ValidationError('La descripción del color debe tener entre 5 y 250 caracteres.')