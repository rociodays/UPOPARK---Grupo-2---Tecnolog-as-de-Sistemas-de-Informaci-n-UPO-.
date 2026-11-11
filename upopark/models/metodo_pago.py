from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MetodoPago(models.Model):
    _name = 'upopark.metodo_pago'
    _description = 'Método de Pago'
    _rec_name = 'metodo'

    metodo = fields.Char(string='Método', required=True)
    comision = fields.Float(string='Comisión')
    descripcion = fields.Text(string='Descripción')

    entidad_bancaria_ids = fields.Many2many(
        'upopark.entidad_bancaria',
        'upopark_entidad_metodo_rel', 'metodo_id', 'entidad_id',
        string='Entidades Bancarias',
    )

    @api.constrains('comision')
    def _check_comision(self):
        for record in self:
            if not 0 <= record.comision <= 100:
                raise ValidationError('La comisión debe estar entre 0 y 100 %.')