from odoo import models, fields

class MaterialPavimento(models.Model):
    _name = 'upopark.material_pavimento'
    _description = 'Material de pavimento del que está hecho un aparcamiento'

    material = fields.Char(string='Material', size=60, required=True)
    descripcion = fields.Char(string='Descripción', size=60, required=True)

    aparcamiento_ids = fields.One2many('upopark.aparcamiento', 'material_pavimento_id', string='Aparcamientos')