from odoo import models, fields, api

class TipoConector(models.Model):
    _name = 'upopark.tipo_conector'
    _description = 'Tipo de Conector'

    name = fields.Char(string='Tipo', required=True)
    nombre = fields.Char(string='Nombre')
    corriente = fields.Selection([
        ('ca', 'Corriente Alterna'),
        ('cc', 'Corriente Continua')
    ], string='Corriente')
    conector_ids = fields.One2many('upopark.conector', 'tipo_conector_id', string='Conectores')