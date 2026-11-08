from odoo import models, fields, api
class Alegacion(models.Model):
    _name = 'upopark.alegacion'
    _description = 'Alegación Administrativa'

    name = fields.Char(string='Nº Registro Alegación', required=True)
    argumento = fields.Text(string='Cuerpo de la Alegación')
    estado = fields.Selection([('pendiente', 'Pendiente'), ('resuelta', 'Resuelta')], string='Estado', default='pendiente')

    usuario_id = fields.Many2one('upopark.usuario', string='Usuario que alega', required=True)