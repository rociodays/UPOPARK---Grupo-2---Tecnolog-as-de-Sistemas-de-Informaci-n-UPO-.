from odoo import models, fields, api

class EstadoEstancia(models.Model):
    _name = 'upopark.estado_estancia'
    _description = 'Estado de la Estancia'

    name = fields.Char(string='Estado', required=True)
    descripcion = fields.Text(string='Descripción')
    estancia_ids = fields.One2many('upopark.estancia', 'estado_estancia_id', string='Estancias')