from odoo import models, fields, api

class Usuario(models.Model):
    _name = 'upopark.usuario'
    _description = 'Usuario del Parking'

    name = fields.Char(string='Nombre Completo', required=True)
    dni = fields.Char(string='DNI', required=True)
    email = fields.Char(string='Correo Electrónico')

    organizacion_id = fields.Many2one('upopark.organizacion', string='Organización')
    permiso_ids = fields.One2many('upopark.permiso_acceso', 'usuario_id', string='Permisos')
    sesion_ids = fields.One2many('upopark.sesion_recarga', 'usuario_id', string='Sesiones de Recarga')
    alegacion_ids = fields.One2many('upopark.alegacion', 'usuario_id', string='Alegaciones')