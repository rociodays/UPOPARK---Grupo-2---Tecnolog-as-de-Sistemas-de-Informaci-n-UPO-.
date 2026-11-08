from odoo import models, fields, api

class TicketSoporte(models.Model):
    _name = 'upopark.ticket_soporte'
    _description = 'Tickets de Soporte'

    referencia = fields.Char(string='Referencia', required=True)
    asunto = fields.Char(string='Asunto', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha_creacion = fields.Datetime(string='Fecha de Creación', default=fields.Datetime.now)
    
    prioridad_id = fields.Many2one('upopark.prioridad', string='Prioridad')
    contacto_id = fields.Many2one('upopark.contacto', string='Contacto')
    mensaje_ids = fields.One2many('upopark.mensaje_ticket', 'ticket_id', string='Mensajes')