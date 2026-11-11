from odoo import models, fields, api

class EstadoEstacionRecarga(models.Model):
    _name = 'upopark.estado_estacion_recarga'
    _description = 'Estado Estación de Recarga'

    name = fields.Char(string='Estado', required=True)
    descripcion = fields.Text(string='Descripción')
    estacion_ids = fields.One2many('upopark.estacion_recarga', 'estado_estacion_id', string='Estaciones de Recarga')