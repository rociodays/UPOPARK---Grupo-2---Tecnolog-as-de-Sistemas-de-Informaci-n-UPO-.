from odoo import models, fields

class BloqueoPlaza(models.Model):
    _name = 'upopark.bloqueo_plaza'
    _description = 'Situación de bloqueo de una plaza'

    referencia = fields.Char(string='Referencia', size=9, required=True)
    inicio = fields.Datetime(string='Comienzo', required=True, default=fields.Datetime.now)
    fin = fields.Datetime(string='Final', required=True)
    activo = fields.Boolean(string='¿Bloqueo en estado activo?', default=False)

    bloqueo_plaza_plaza = fields.Many2one('upopark.plaza', string='Plaza afectada')
    bloqueo_plaza_motivo_bloqueo = fields.Many2one('upopark.motivo_bloqueo', string='Motivo del bloqueo')