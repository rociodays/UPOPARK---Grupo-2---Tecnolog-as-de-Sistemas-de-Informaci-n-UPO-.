from odoo import models, fields

class NivelAcceso(models.Model):
    _name = 'upopark.nivel_acceso'
    _description = 'Grado de acceso requerido para entrar en una zona'

    nivel = fields.Integer(string='Nivel', required=True)
    descripcion = fields.Char(string='Descripción', size=60, required=True)

    nivel_acceso_zona = fields.One2many('upopark.zona', 'zona_nivel_acceso', string='Zonas')