from odoo import models, fields, api

class FranjaCalendario(models.Model):
    _name = 'upopark.franja_calendario'
    _description = 'Franjas de Calendario'

    dia_semana = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo')
    ], string='Día de la Semana', required=True)
    hora_desde = fields.Char(string='Hora Desde')
    hora_hasta = fields.Char(string='Hora Hasta')
    
    calendario_id = fields.Many2one('upopark.calendario', string='Calendario', required=True)