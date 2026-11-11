from odoo import models, fields

class Festivo(models.Model):
    _name = 'upopark.festivo'
    _description = 'Festivo'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    calendario_id = fields.Many2one('upopark.calendario', string='Calendario')