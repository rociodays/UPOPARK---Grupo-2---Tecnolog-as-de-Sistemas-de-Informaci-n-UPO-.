from odoo import models, fields, api

class ResumenDiario(models.Model):
    _name = 'upopark.resumen_diario'
    _description = 'Resumen Diario de Ocupación'

    dia = fields.Date(string='Día', required=True)
    min_ocup = fields.Integer(string='Ocupación Mínima')
    pico_ocup = fields.Integer(string='Pico de Ocupación')
    ratio_med = fields.Float(string='Ratio Medio')
    
    estancia_id = fields.Many2one('upoPark.estancia', string='Estancia')