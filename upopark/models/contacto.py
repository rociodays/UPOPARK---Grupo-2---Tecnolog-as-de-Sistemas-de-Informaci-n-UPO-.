from odoo import models, fields, api

class Contacto(models.Model):
    _name = 'upopark.contacto'
    _description = 'Gestión de Contactos'

    nombre = fields.Char(string='Nombre', required=True)
    num_doc = fields.Char(string='Número de Documento', required=True)
    telefono = fields.Char(string='Teléfono')
    correo = fields.Char(string='Correo Electrónico')
    
    tipo_doc_id = fields.Many2one('upopark.tipo_doc', string='Tipo de Documento')
    usuario_id = fields.Many2one('upopark.usuario', string='Usuario del Sistema')
    organizacion_id = fields.Many2one('upopark.organizacion', string='Organización')

    cargo_ids = fields.One2many('upopark.cargo', 'contacto_id', string='Cargos')
    sancion_ids = fields.One2many('upopark.sancion', 'contacto_id', string='Sanciones')
    incidencia_ids = fields.One2many('upopark.mantenimiento.incidencia', 'contacto_id', string='Incidencias')
    ticket_ids = fields.One2many('upopark.ticket_soporte', 'contacto_id', string='Tickets')
    mensaje_ids = fields.One2many('upopark.mensaje_ticket', 'contacto_id', string='Mensajes')
