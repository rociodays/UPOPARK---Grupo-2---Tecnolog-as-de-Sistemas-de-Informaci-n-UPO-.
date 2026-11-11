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

    #validaciones
    #longitud de la descripcion
    @api.constrains('cDescripcion')
    def _check_longitud_descripcion_tipo(self):
        for record in self:
            if record.cDescripcion:
                if len(record.cDescripcion) < 5 or len(record.cDescripcion) > 250:
                    raise models.ValidationError('La descripcion del tipo de vehiculo debe tener entre 5 y 250 caracteres.')