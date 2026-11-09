from odoo import model, fields, api

class EstadoCargo(models.Model):
    _name = 'upopark.estado_cargo'
    _description = 'Estado de Cargo'

    estado = fields.Selection([('pagado', 'Pagado'), ('pendiente', 'Pendiente')], string='Estado', required=True, default='pendiente')
    descripcion = fields.Char(string='Descripcion')