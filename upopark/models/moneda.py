from odoo import models, fields, api


class Moneda(models.Model):
    _name = 'upopark.moneda'
    _description = 'Moneda'

    name = fields.Char(string='Código ISO (Ej. EUR)', required=True)
    simbolo = fields.Char(string='Símbolo', required=True)
    tasa_cambio = fields.Float(string='Tasa de Cambio')

    tarifa_ids = fields.One2many('upopark.tarifa', 'moneda_id', string='Tarifas')