from odoo import models, fields, api
class EstacionRecarga(models.Model):
    _name = 'upopark.estacion_recarga'
    _description = 'Estación de Recarga EV'

    name = fields.Char(string='Nombre/Código Estación', required=True)
    estado = fields.Selection([('operativa', 'Operativa'), ('mantenimiento', 'En Mantenimiento')], string='Estado')

    conector_ids = fields.One2many('upopark.conector', 'estacion_id', string='Conectores')