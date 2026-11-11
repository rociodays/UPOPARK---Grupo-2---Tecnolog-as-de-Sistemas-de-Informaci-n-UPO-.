from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MetodoPago(models.Model):
    _name = 'upopark.metodo_pago'
    _description = 'Método de Pago'
    _rec_name = 'smetodo'

    smetodo = fields.Char(string='Método', required=True)
    fcomision = fields.Float(string='Comisión')
    sdescripcion = fields.Text(string='Descripción')
    entidad_bancaria_ids = fields.Many2many(
        'upopark.entidad_bancaria',
        'upopark_entidad_metodo_rel', 'metodo_id', 'entidad_id',
        string='Entidades Bancarias',
    )
    @api.constrains('fcomision')
    def _check_comision(self):
        for record in self:
            if record.fcomision < 0 or record.fcomision > 100:
                raise ValidationError('La comisión debe estar entre 0 y 100 %.')
