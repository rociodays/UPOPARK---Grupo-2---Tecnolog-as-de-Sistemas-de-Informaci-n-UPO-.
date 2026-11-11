from odoo import models, fields

class Zona(models.Model):
    _name = 'upopark.zona'
    _description = 'Una de las zonas en que se divide la universidad'

    nombre = fields.Char(string='Nombre Zona', size=60, required=True)
    codigo = fields.Char(string='Codigo', size=9, required=True)

    zona_nivel_acceso = fields.Many2one('upopark.nivel_acceso', string='Nivel de acceso requerido')
    zona_aparcamiento = fields.One2many('upopark.aparcamiento', 'aparcamiento_zona', string='Aparcamientos')