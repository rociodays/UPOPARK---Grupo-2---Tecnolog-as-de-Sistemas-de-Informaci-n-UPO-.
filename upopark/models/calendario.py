from odoo import models, fields

class Calendario(models.Model):
    _name = 'upopark.calendario'
    _description = 'Calendario Base'

    codigo = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    zona_horaria = fields.Char(string='Zona Horaria')
    activo = fields.Boolean(string='Activo', default=True)
    organizacion_id = fields.Many2one('upopark.organizacion', string='Organización')

    franja_ids = fields.One2many('upopark.franja_calendario', 'calendario_id', string='Franjas Horarias')
    recurso_ids = fields.One2many('upopark.recurso', 'calendario_id', string='Recursos')
    evento_ids = fields.One2many('upopark.evento_campus', 'calendario_id', string='Eventos')
    festivo_ids = fields.One2many('upopark.festivo', 'calendario_id', string='Festivos')