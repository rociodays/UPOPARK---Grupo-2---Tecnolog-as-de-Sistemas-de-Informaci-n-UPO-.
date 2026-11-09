from odoo import models, fields, api

class Prioridad(models.Model):
    _name = 'upopark.prioridad'
    _description = 'Prioridad de Tickets'

    nombre = fields.Char(string='Prioridad', required=True)
    descripcion = fields.Char(string='Descripción')
    
    ticket_ids = fields.One2many('upopark.ticket_soporte', 'prioridad_id', string='Tickets')