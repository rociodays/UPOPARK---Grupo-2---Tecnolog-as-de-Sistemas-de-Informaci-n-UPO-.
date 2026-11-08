from odoo import models, fields, api
class PermisoAcceso(models.Model):
    _name = 'upopark.permiso_acceso'
    _description = 'Permiso de Acceso'

    name = fields.Char(string='Código de Permiso', required=True)
    fecha_inicio = fields.Datetime(string='Válido desde', required=True)
    fecha_fin = fields.Datetime(string='Válido hasta', required=True)

    usuario_id = fields.Many2one('upopark.usuario', string='Usuario Autorizado', required=True)
    punto_acceso_id = fields.Many2one('upopark.punto_acceso', string='Punto de Acceso', required=True)