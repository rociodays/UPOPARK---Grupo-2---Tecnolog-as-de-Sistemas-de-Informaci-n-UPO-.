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

    #sql constraints
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'El color ya está registrado.')
    ]

    #validaciones
    @api.constrains('cDescripcion')
    def _check_longitud_descripcion_color(self):
        for record in self:
            if record.cDescripcion:
                if len(record.cDescripcion) < 5 or len(record.cDescripcion) > 250:
                    raise models.ValidationError('La descripcion del color debe tener entre 5 y 250 caracteres.')
