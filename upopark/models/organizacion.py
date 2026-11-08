from odoo import models, fields, api

class Organizacion(models.Model):
    _name = 'upopark.organizacion'
    _description = 'Organización / Empresa'

    name = fields.Char(string='Nombre de Organización', required=True)
    cif = fields.Char(string='CIF', required=True)

    usuario_ids = fields.One2many('upopark.usuario', 'organizacion_id', string='Usuarios Asociados')