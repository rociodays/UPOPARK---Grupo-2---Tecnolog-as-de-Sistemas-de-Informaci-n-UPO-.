from odoo import models, fields, api

class PuntoAcceso(models.Model):
    _name = 'upopark.punto_acceso'
    _description = 'Punto de Acceso Físico'

    name = fields.Char(string='Código de Barrera/Acceso', required=True)
    ubicacion = fields.Char(string='Ubicación')
    tipo = fields.Selection([('vehiculo', 'Barrera Vehículos'), ('peatonal', 'Torno Peatonal')], string='Tipo')

    estado_punto_acceso_id = fields.Many2one('upopark.estado_punto_acceso', string='Estado del Punto de Acceso')

    permiso_ids = fields.One2many('upopark.permiso_acceso', 'punto_acceso_id', string='Permisos Vinculados')