from odoo import models, fields, api

class Estancia(models.Model):
    _name = 'upopark.estancia'
    _description = 'Estancia'

    referencia = fields.Char(string='Referencia', required=True)
    entrada = fields.Datetime(string='Entrada', required=True)
    salida = fields.Datetime(string='Salida', required=True)

    punto_acceso_comienza_ids = fields.One2many('upopark.punto_acceso', 'estancia_comienza_id', string='Puntos de Acceso (Comienza)')
    punto_acceso_finaliza_ids = fields.One2many('upopark.punto_acceso', 'estancia_finaliza_id', string='Puntos de Acceso (Finaliza)')
    sesion_carga_id = fields.Many2one('upopark.sesion_carga', string='Sesion de Carga')
    conector_id = fields.Many2one('upopark.conector', string='Conector')
    cargo_id = fields.Many2one('upopark.cargo', string='Cargo', required=True)
    estado_estancia_id = fields.Many2one('upopark.estado_estancia', string='Estado Estancia', required=True)