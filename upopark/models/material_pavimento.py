from odoo import models, fields, api

class MaterialPavimento(models.Model):
    
    _name = 'upopark.material_pavimento'
    _description = 'Material de pavimento del que está hecho un aparcamiento'

    material = fields.Char('Material', size=60, required=True)
    descripcion = fields.Char('Estado', size=60, required=True)

    material_pavimento_aparcamiento = fields.One2many('upopark.aparcamiento', 'MaterialPavimento es suelo de Aparcamiento')
