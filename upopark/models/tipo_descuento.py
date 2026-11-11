from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TipoDescuento(models.Model):
    _name = 'upopark.tipo_descuento'
    _description = 'Tipo de Descuento'
    _rec_name = 'snombre'

    scodigo = fields.Char(string='Código', required=True)
    snombre = fields.Char(string='Nombre', required=True)
    fporcentaje = fields.Float(string='Porcentaje')
    descuento_asignado_ids = fields.One2many(
        'upopark.descuento_asignado', 'tipo_descuento_id',
        string='Descuentos Asignados',
    )
    @api.constrains('fporcentaje')
    def _check_porcentaje(self):
        for record in self:
            if record.fporcentaje < 0 or record.fporcentaje > 100:
                raise ValidationError('El porcentaje de descuento debe estar entre 0 y 100 %.')
