from odoo import models, fields

class Cargo(models.Model):
    _name = 'upopark.cargo'
    _description = 'Cargo'

    referencia = fields.Char(string='Referencia', required=True)
    emision = fields.Datetime(string='Emisión', required=True)
    importe = fields.Monetary(string='Importe Total', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Moneda')

    tipo_servicio_cargo_id = fields.Many2one('upopark.tipo_servicio_cargo', string='Tipo de Servicio', required=True)
    linea_cargo_id = fields.Many2one('upopark.linea_cargo', string='Línea', required=True)
    estado_cargo_id = fields.Many2one('upopark.estado_cargo', string='Estado', required=True)
    contacto_id = fields.Many2one('upopark.contacto', string='Contacto', required=True)
    plazo_pago_id = fields.Many2one('upopark.plazo_pago', string='Plazo de Pago')
    sesion_carga_id = fields.Many2one('upopark.sesion_recarga', string='Sesión de recarga')
    estancia_ids = fields.One2many('upopark.estancia', 'cargo_id', string='Estancias')
    metodo_pago_ids = fields.Many2many('upopark.metodo_pago', string='Métodos de Pago')