from odoo import models, fields

class EstadoCargo(models.Model):
    _name = 'upopark.estado_cargo'
    _description = 'Estado de Cargo'

    estado = fields.Selection([('pagado', 'Pagado'), ('pendiente', 'Pendiente')], string='Estado', required=True, default='pendiente')
    descripcion = fields.Char(string='Descripción')