from odoo import models, fields, api

class Conector(models.Model):
    _name = 'upopark.conector'
    _description = 'Conector de Estación'

    name = fields.Char(string='ID Conector (ej. CCS2-01)', required=True)
    potencia_kw = fields.Float(string='Potencia Máxima (kW)')

    estado_conector_id = fields.Many2one('upopark.estado_conector', string='Estado del Conector')
    estacion_id = fields.Many2one('upopark.estacion_recarga', string='Estación de Recarga')
    tipo_conector_id = fields.Many2one('upopark.tipo_conector', string='Tipo de Conector')
    sesion_ids = fields.One2many('upopark.sesion_recarga', 'conector_id', string='Historial de Sesiones')