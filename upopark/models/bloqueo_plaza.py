from odoo import models, fields, api

class BloqueoPlaza(models.Model):
    
    _name = 'upopark.bloqueo_plaza'
    _description = 'Situación de bloqueo de una plaza'

    referencia = fields.Char('Referencia', size=9, required=True)
    inicio = fields.Datetime('Comienzo', required=True, autodate = True)
    fin = fields.Datetime('Final', required=True, autodate = True)
    
    activo = fields.Boolean(
            string='¿Bloqueo en estado activo?',
            default=False
        )

    bloqueo_plaza_plaza = fields.Many2one('upopark.plaza', 'BloqueoPlaza afecta a Plaza')
    bloqueo_plaza_motivo_bloqueo = fields.Many2one('upopark.motivo_bloqueo', 'BloqueoPlaza se debe a MotivoBloqueo')
    bloqueo_plaza_incidencia = fields.Many2one('upopark.incidencia', 'BloqueoPlaza se debe a Incidencia')
