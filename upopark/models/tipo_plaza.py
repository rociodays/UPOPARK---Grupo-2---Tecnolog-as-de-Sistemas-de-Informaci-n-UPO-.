from odoo import models, fields

class TipoPlaza(models.Model):
    _name = 'upopark.tipo_plaza'
    _description = 'Tipo de plaza'

    codigo = fields.Char(string='Código', size=9, required=True)
    nombre = fields.Char(string='Nombre', size=9, required=True)
    requiere_vehiculo_electrico = fields.Boolean(string='¿Requiere vehículo eléctrico?', default=False)
    accesible = fields.Boolean(string='¿Es una plaza accesible?', default=False)

    plaza_ids = fields.One2many('upopark.plaza', 'tipo_plaza_id', string='Plazas')
    tipo_plaza_organizacion = fields.Many2one('upopark.organizacion', string='Organización')