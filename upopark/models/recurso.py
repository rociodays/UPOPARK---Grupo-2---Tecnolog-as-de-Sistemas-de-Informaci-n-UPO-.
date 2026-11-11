from odoo import models, fields, api

class Recurso(models.Model):
    _name = 'upopark.recurso'
    _description = 'Recurso'
    _order = 'codigo, nombre'
    _rec_name = 'nombre'

    codigo = fields.Char(string='Codigo', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    active = fields.Boolean(string='Activo', default=True)

    organizacion_id = fields.Many2one('upopark.organizacion', string='Organizacion', required=True)
    tipo_recurso_id = fields.Many2one('upopark.tipo_recurso', string='Tipo de recurso', required=True)
    calendario_id = fields.Many2one('upopark.calendario', string='Calendario')