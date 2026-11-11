from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DescuentoAsignado(models.Model):
    _name = 'upopark.descuento_asignado'
    _description = 'Descuento Asignado'
    _rec_name = 'num_doc'

    codigo_tipo_descuento = fields.Char(string='Cód. Tipo Descuento')
    tipo_doc = fields.Char(string='Tipo Doc.')
    num_doc = fields.Char(string='Núm. Doc.', required=True)
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_fin = fields.Date(string='Fecha Fin')
    activo = fields.Boolean(string='Activo', default=True)

    tipo_descuento_id = fields.Many2one(
        'upopark.tipo_descuento', string='Tipo de Descuento', required=True, ondelete='restrict',
    )

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas_descuento(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin and record.fecha_fin < record.fecha_inicio:
                raise ValidationError('La fecha de fin del descuento no puede ser anterior a la de inicio.')

    def btn_activar(self):
        self.write({'activo': True})

    def btn_desactivar(self):
        self.write({'activo': False})