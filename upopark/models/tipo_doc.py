from odoo import models, fields, api

class TipoDoc(models.Model):
    _name = 'upopark.tipo_doc'
    _description = 'Tipos de Documento'

    nombre = fields.Char(string='Tipo de Documento', required=True)
    descripcion = fields.Char(string='Descripción')