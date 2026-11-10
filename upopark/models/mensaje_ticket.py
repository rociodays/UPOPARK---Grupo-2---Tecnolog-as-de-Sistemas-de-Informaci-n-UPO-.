from odoo import models, fields, api

class MensajeTicket(models.Model):
    _name = 'upopark.mensaje_ticket'
    _description = 'Mensajes de los Tickets'

    fecha_hora = fields.Datetime(string='Fecha y Hora', default=fields.Datetime.now)
    texto = fields.Text(string='Texto')
    comentario = fields.Char(string='Comentario')
    
    ticket_id = fields.Many2one('upopark.ticket_soporte', string='Ticket', required=True)
    contacto_id = fields.Many2one('upopark.contacto', string='Entregado a')
