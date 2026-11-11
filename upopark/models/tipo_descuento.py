from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TipoDescuento(models.Model):
    _name = 'upopark.tipo_descuento'
    _description = 'Tipo de Descuento'
    _rec_name = 'nombre'

    codigo = fields.Char(string='Código', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    porcentaje = fields.Float(string='Porcentaje')

    descuento_asignado_ids = fields.One2many(
        'upopark.descuento_asignado', 'tipo_descuento_id', string='Descuentos Asignados',
    )

    @api.constrains('porcentaje')
    def _check_porcentaje(self):
        for record in self:
            if not 0 <= record.porcentaje <= 100:
                raise ValidationError('El porcentaje de descuento debe estar entre 0 y 100 %.')