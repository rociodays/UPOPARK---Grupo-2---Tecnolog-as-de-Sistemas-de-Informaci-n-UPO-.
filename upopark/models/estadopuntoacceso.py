from odoo import models, fields, api

class EstadoPuntoAcceso(models.Model):
    _name = 'upopark.estado_punto_acceso'
    _description = 'Estado Punto de Acceso'

    name = fields.Char(string='Estado', required=True)
    descripcion = fields.Text(string='Descripción')
    punto_acceso_ids = fields.One2many('upopark.punto_acceso', 'estado_punto_acceso_id', string='Puntos de Acceso')