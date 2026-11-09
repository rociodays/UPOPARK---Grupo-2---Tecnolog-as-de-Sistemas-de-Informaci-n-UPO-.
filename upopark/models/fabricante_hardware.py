from odoo import models, fields, api

class FabricanteHardware(models.Model):
    _name = 'upopark.fabricante_hardware'
    _description = 'Fabricante de Hardware'

    nombre = fields.Char(string='Nombre', required=True)
    soporte_tecnico = fields.Char(string='Soporte Tecnico', required=True)
    web = fields.Char(string='Sitio Web')

    conector_ids = fields.One2many('upopark.conector', 'fabricante_hardware_id', string='Conectores')