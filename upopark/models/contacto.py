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