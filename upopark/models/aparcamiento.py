from odoo import models, fields, api

class Aparcamiento(models.Model):
    
    _name = 'upopark.aparcamiento'
    _description = 'Uno de los aparcaminento de la Universidad'
    
    nombre = fields.Char(string="Nombre Aparcamiento", size=60, required=True, help="El nombre del aparcamiento")
    codigo = fields.Char('Código', size=9, required=True)
    capacidad = fields.Integer("Capacidad")
    activo = fields.Boolean(
            string='¿Parking en estado activo?',
            default=True
        )
        
    aparcamiento_campus = fields.Many2one('upopark.campus', 'Aparcamiento gestionado en Campus')
    aparcamiento_zona = fields.Many2one('upopark.zona','Aparcamiento pertenece a Zona')
    aparcamiento_plaza = fields.One2many('upopark.plaza', 'Aparcamiento posee Plazas')
