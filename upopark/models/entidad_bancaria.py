from odoo import models, fields


class EntidadBancaria(models.Model):
    _name = 'upopark.entidad_bancaria'
    _description = 'Entidad Bancaria'
    _rec_name = 'snombre'

    scodigo = fields.Char(string='Código', required=True)
    snombre = fields.Char(string='Nombre', required=True)
    sbic = fields.Char(string='BIC')
    # Relación Registra: (1,N) / (0,N), representada como N:M.
    metodo_pago_ids = fields.Many2many(
        'upopark.metodo_pago',
        'upopark_entidad_metodo_rel', 'entidad_id', 'metodo_id',
        string='Métodos de Pago',
    )
