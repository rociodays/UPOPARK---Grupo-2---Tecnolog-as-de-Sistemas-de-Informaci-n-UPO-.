from odoo import models, fields, api

class EstadoConservacionPlaza(models.Model):
    
    _name = 'upopark.estado_conservacion_plaza'
    _description = 'Estado de conservacion de una plaza'

    estado = fields.Char('Estado', size=9, required=True)
    activo = fields.Boolean(
            string='¿Estado activo?',
            default=True
        )
        
    estadoPlaza_plaza = fields.One2many('upopark.plaza', 'EstadoPlaza muestra condicion de Plaza')
    estadoPlaza_indisponibilidad = fields.Many2one('upopark.indisponibilidad', 'EstadoPlaza puede generar Indisponibilidad')
    estadoPlaza_incidencia = fields.Many2one('upopark.incidencia', 'EstadoPlaza puede generar Incidencia')
