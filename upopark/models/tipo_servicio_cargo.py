from odoo import models, fields, api

class TipoServicioCargo(models.Model):
    _name = 'upopark.tipo_servicio_cargo'
    _description = 'Tipo de servicio de Cargo'

    tipo = fields.Char(string='Tipo', required=True)
    descripcion = fields.Char(string='Descripcion')

    cargo_id = fields.One2Many('upopark.cargo', string='Cargos')