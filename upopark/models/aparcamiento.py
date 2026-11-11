from odoo import models, fields

class Aparcamiento(models.Model):
    _name = 'upopark.aparcamiento'
    _description = 'Uno de los aparcamientos de la Universidad'

    nombre = fields.Char(string='Nombre Aparcamiento', size=60, required=True)
    codigo = fields.Char(string='Código', size=9, required=True)
    capacidad = fields.Integer(string='Capacidad')
    activo = fields.Boolean(string='¿Parking en estado activo?', default=True)

    aparcamiento_campus = fields.Many2one('upopark.campus', string='Aparcamiento gestionado en Campus')
    aparcamiento_zona = fields.Many2one('upopark.zona', string='Aparcamiento pertenece a Zona')
    material_pavimento_id = fields.Many2one('upopark.material_pavimento', string='Material del pavimento')

    aparcamiento_plaza = fields.One2many('upopark.plaza', 'plaza_aparcamiento', string='Plazas')