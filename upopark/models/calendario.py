from odoo import models, fields, api

class Calendario(models.Model):
    _name = 'upopark.calendario'
    _description = 'Calendario Base'

    codigo = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    zona_horaria = fields.Char(string='Zona Horaria')
    activo = fields.Boolean(string='Activo', default=True)
    
    organizacion_id = fields.Many2one('upoPark.organizacion', string='Organización')
    franja_ids = fields.One2many('upopark.franja_calendario', 'calendario_id', string='Franjas Horarias')