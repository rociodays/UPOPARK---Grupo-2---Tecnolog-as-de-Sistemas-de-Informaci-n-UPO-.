from odoo import models, fields

class EstadoConservacionPlaza(models.Model):
    _name = 'upopark.estado_conservacion_plaza'
    _description = 'Estado de conservación de una plaza'

    estado = fields.Char(string='Estado', size=9, required=True)
    activo = fields.Boolean(string='¿Estado activo?', default=True)

    plaza_ids = fields.One2many('upopark.plaza', 'plaza_estado_conservacion', string='Plazas')