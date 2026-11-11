from odoo import models, fields

class EntidadBancaria(models.Model):
    _name = 'upopark.entidad_bancaria'
    _description = 'Entidad Bancaria'
    _rec_name = 'nombre'

    codigo = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    bic = fields.Char(string='BIC')

    metodo_pago_ids = fields.Many2many(
        'upopark.metodo_pago',
        'upopark_entidad_metodo_rel', 'entidad_id', 'metodo_id',
        string='Métodos de Pago',
    )