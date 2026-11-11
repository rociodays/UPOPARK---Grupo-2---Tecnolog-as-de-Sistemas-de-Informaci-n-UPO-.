from odoo import models, fields, api

class TipoRecurso(models.Model):
    _name = 'upopark.tipo_recurso'
    _description = 'Tipo de Recurso'

    name = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    recurso_ids = fields.One2many('upopark.recurso', 'tipo_recurso_id', string='Recursos')