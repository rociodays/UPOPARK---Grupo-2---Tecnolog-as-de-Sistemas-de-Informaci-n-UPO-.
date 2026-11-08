from odoo import models, fields, api
class LineaCargo(models.Model):
    _name = 'upopark.linea_cargo'
    _description = 'Línea de Cargo / Facturación'

    name = fields.Char(string='Concepto de Cargo', required=True)
    importe_total = fields.Float(string="Importe Total (€)", required=True)

    sesion_id = fields.Many2one('upopark.sesion_recarga', string='Sesión Vinculada')
    tarifa_id = fields.Many2one('upopark.tarifa', string='Tarifa Aplicada', required=True)