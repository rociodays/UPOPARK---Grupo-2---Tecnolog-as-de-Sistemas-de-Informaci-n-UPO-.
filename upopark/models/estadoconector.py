from odoo import models, fields, api

class EstadoConector(models.Model):
    _name = 'upopark.estado_conector'
    _description = 'Estado del Conector'

    name = fields.Char(string='Estado', required=True)
    descripcion = fields.Text(string='Descripción')
    conector_ids = fields.One2many('upopark.conector', 'estado_conector_id', string='Conectores')