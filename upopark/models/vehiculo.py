from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Vehiculo(models.Model):
    _name = 'upopark.vehiculo'
    _description = 'Vehiculo'

    name = fields.Char(string='Matrícula', required=True)
    pais_matricula = fields.Char(string='País Matrícula', required=True)
    numero_puertas = fields.Integer(string='Número de Puertas')
    tiene_remolque = fields.Boolean(string='Tiene Remolque')

    color_vehiculo_id = fields.Many2one('upopark.color_vehiculo', string='Color')
    tipo_vehiculo_id = fields.Many2one('upopark.tipo_vehiculo', string='Tipo de Vehículo', required=True)
    modelo_vehiculo_id = fields.Many2one('upopark.modelo_vehiculo', string='Modelo')
    etiqueta_ambiental_id = fields.Many2one('upopark.etiqueta_ambiental', string='Etiqueta Ambiental')
    tipo_combustible_id = fields.Many2one('upopark.tipo_combustible', string='Tipo de Combustible', required=True)
    contacto_id = fields.Many2one('upopark.contacto', string='Contacto', required=True)
    marca_vehiculo_id = fields.Many2one('upopark.marca_vehiculo', string='Marca')

    conector_ids = fields.Many2many('upopark.conector', string='Conectores Compatibles')

    restriccion_ids = fields.One2many('upopark.restriccion_acceso', 'vehiculo_id', string='Historial de Restricciones')
    reserva_ids = fields.One2many('upopark.reserva', 'vehiculo_id', string='Historial de Reservas')
    infraccion_ids = fields.One2many('upopark.infraccion', 'vehiculo_id', string='Historial de Infracciones')

    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'La matrícula del vehículo ya está registrada.')]

    @api.constrains('name')
    def _check_formato_matricula(self):
        for record in self:
            if record.name and not re.match(r'^[A-Z0-9]{4,10}$', record.name):
                raise ValidationError('El formato de la matrícula es incorrecto.')

    @api.constrains('numero_puertas')
    def _check_rango_puertas(self):
        for record in self:
            if record.numero_puertas and not 0 <= record.numero_puertas <= 5:
                raise ValidationError('El vehículo no puede tener menos de 0 ni más de 5 puertas.')

    @api.constrains('tipo_combustible_id', 'conector_ids')
    def _check_combustible_conectores(self):
        for record in self:
            if record.tipo_combustible_id and record.conector_ids:
                if record.tipo_combustible_id.nombre.lower() != 'electrico':
                    raise ValidationError('Solo los vehículos eléctricos pueden tener conectores asignados.')