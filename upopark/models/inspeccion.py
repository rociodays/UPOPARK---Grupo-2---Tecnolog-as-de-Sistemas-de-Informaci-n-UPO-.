from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Inspeccion(models.Model):
    _name = 'upopark.inspeccion'
    _description = 'Inspección de mantenimiento'
    _rec_name = 'strReferencia'
    _order = 'id desc'
    _sql_constraints = [
        ('reference_unique', 'UNIQUE("strReferencia")', 'La referencia de la inspección ya existe.'),
    ]

    strReferencia = fields.Char(string='Referencia', required=True, readonly=True, copy=False)
    orden_trabajo_id = fields.Many2one(
        'upopark.orden_trabajo', string='Orden de trabajo',
        required=True, ondelete='restrict', index=True,
    )
    indisponibilidad_id = fields.Many2one(
        'upopark.indisponibilidad', string='Indisponibilidad documentada',
        ondelete='restrict', index=True,
    )
    inspector_id = fields.Many2one(
        'res.partner', string='Persona que realiza la inspección', ondelete='restrict',
    )
    dateFechaInspeccion = fields.Date(string='Fecha de inspección')
    resultado_id = fields.Many2one(
        'upopark.resultado', string='Resultado general',
        ondelete='restrict',
    )
    strObservaciones = fields.Text(string='Observaciones')
    elemento_inspeccionado_ids = fields.One2many(
        'upopark.elemento_inspeccionado', 'inspeccion_id',
        string='Puntos de comprobación', copy=False,
    )

    @api.model_create_multi
    def create(self, lstValores):
        return super().create([
            dict(dictValores, strReferencia=self.env['ir.sequence'].next_by_code('upopark.inspeccion'))
            for dictValores in lstValores
        ])

    @api.constrains('inspector_id', 'dateFechaInspeccion', 'resultado_id')
    def _comprobar_inspeccion_completada(self):
        for rsInspeccion in self:
            if rsInspeccion.resultado_id and not (rsInspeccion.inspector_id and rsInspeccion.dateFechaInspeccion):
                raise ValidationError('Indica quién realizó la inspección y en qué fecha antes de guardar su resultado.')
