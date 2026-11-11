from odoo import models, fields

class Campus(models.Model):
    _name = 'upopark.campus'
    _description = 'Campus Universitario'

    nombre = fields.Char(string='Nombre Campus', size=60, required=True)
    codigo = fields.Char(string='Código', size=9, required=True)
    direccion = fields.Char(string='Dirección', size=60, required=True)
    latitud = fields.Char(string='Latitud', size=9, required=True)
    longitud = fields.Char(string='Longitud', size=9, required=True)

    campus_organizacion = fields.Many2one('upopark.organizacion', string='Organización')
    campus_aparcamiento = fields.One2many('upopark.aparcamiento', 'aparcamiento_campus', string='Aparcamientos')