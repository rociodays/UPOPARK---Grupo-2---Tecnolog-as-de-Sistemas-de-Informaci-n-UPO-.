from odoo import models, fields, api
class SesionRecarga(models.Model):
    _name = 'upopark.sesion_recarga'
    _description = 'Sesión de Recarga'

    name = fields.Char(string='Referencia de Sesión', required=True)
    fecha = fields.Datetime(string='Fecha y Hora')
    kw_consumidos = fields.Float(string='kW Consumidos', required=True)

    usuario_id = fields.Many2one('upopark.usuario', string='Usuario', required=True)
    conector_id = fields.Many2one('upopark.conector', string='Conector Usado', required=True)
    linea_cargo_ids = fields.One2many('upopark.linea_cargo', 'sesion_id', string='Líneas de Facturación')