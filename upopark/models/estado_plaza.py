from odoo import models, fields

class EstadoPlaza(models.Model):
    _name = 'upopark.estado_plaza'
    _description = 'Estado de una plaza'

    estado = fields.Char(string='Estado', size=9, required=True)
    plaza_ids = fields.One2many('upopark.plaza', 'plaza_estado_plaza', string='Plazas')