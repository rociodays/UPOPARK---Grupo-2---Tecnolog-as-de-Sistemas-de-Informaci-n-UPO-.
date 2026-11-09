from odoo import models, fields, api

class EstadoPermiso(models.Model):
    _name = 'upopark.estado_permiso'
    _description = 'Estado Permiso'

    estado = fields.Selection(
        [('aprobado', 'Aprobado'), ('denegado', 'Denegado'), ('pendiente', 'Pendiente')],
        string='Estado', required=True, default='aprobado')
    descripcion = fields.Char(string='Descripcion')

    permiso_acceso_id = fields.Many2one('upopark.permiso_acceso', string='Permiso de Acceso', required=True)