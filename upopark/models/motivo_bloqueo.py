from odoo import models, fields

class MotivoBloqueo(models.Model):
    _name = 'upopark.motivo_bloqueo'
    _description = 'Motivo de bloqueo de una plaza'

    motivo = fields.Char(string='Motivo', size=60, required=True)
    descripcion = fields.Char(string='Descripción', size=60, required=True)

    bloqueo_plaza_ids = fields.One2many('upopark.bloqueo_plaza', 'bloqueo_plaza_motivo_bloqueo', string='Bloqueos')