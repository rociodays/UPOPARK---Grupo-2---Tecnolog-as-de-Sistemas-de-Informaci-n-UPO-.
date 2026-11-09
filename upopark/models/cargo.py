from odoo import models, fields, api

class Cargo(models.Model):
    _name = 'upopark.cargo'
    _description = 'Cargo'

    referencia = fields.Char(string='Referencia', required=True)
    emision = fields.Datetime(string='Emision', required=True)
    importe = fields.Monetary(string='Importe Total', required=True)

    tipo_servicio_cargo_id = fields.Many2one('upopark.tipo_servicio_cargo', string='Tipo de Servicio', required=True)
    linea_cargo_id = fields.Many2one('upopark.linea_cargo', string='Linea', required=True)
    estado_cargo_id = fields.Many2one('upopark.estado_cargo', string='Estado', required=True)   
    contacto_id = fields.Many2one('upopark.contacto', string='Contacto', required=True)
    estancia_id = fields.Many2one('upopark.estancia', string='Estancia', required=True)
    metodo_pago_id = fields.One2Many('upopark.metodo_pago', string='Metodos de Pago')
    plazo_pago_id = fields.Many2one('upopark.plazo_pago', string='Plazo de Pago')
    sesion_carga_id = fields.Many2one('upopark.sesion_carga', string='Sesiones de Carga', required=True)