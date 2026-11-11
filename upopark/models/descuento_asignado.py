from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DescuentoAsignado(models.Model):
    _name = 'upopark.descuento_asignado'
    _description = 'Descuento Asignado'
    _rec_name = 'snum_doc_co'

    scod_tipo_des = fields.Char(string='Cód. Tipo Des.')
    stipodocco = fields.Char(string='Tipo Doc. Co.')
    snum_doc_co = fields.Char(string='Núm. Doc. Co.', required=True)
    dfechainicio = fields.Date(string='Fecha Inicio')
    dfechafin = fields.Date(string='Fecha Fin')
    bactivo = fields.Boolean(string='Activo', default=True)
    tipo_descuento_id = fields.Many2one(
        'upopark.tipo_descuento', string='Tipo de Descuento', required=True,
        ondelete='restrict',
    )
    @api.constrains('dfechainicio', 'dfechafin')
    def _check_fechas_descuento(self):
        for record in self:
            if (record.dfechainicio and record.dfechafin
                    and record.dfechafin < record.dfechainicio):
                raise ValidationError('La fecha de fin del descuento no puede ser anterior a la fecha de inicio.')

    def btn_activar(self):
        for record in self:
            record.write({'bactivo': True})

    def btn_desactivar(self):
        for record in self:
            record.write({'bactivo': False})
