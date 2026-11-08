from odoo import models, fields, api

class EstacionRecarga(models.Model):
    _name = 'upopark.estacion_recarga'
    _description = 'Estación de Recarga EV'

    name = fields.Char(string='Nombre/Código Estación', required=True)
    estado = fields.Selection([('operativa', 'Operativa'), ('mantenimiento', 'En Mantenimiento')], string='Estado')

    estado_estacion_id = fields.Many2one('upopark.estado_estacion_recarga', string='Estado de la Estación')

    conector_ids = fields.One2many('upopark.conector', 'estacion_id', string='Conectores')
