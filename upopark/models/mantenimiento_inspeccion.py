from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Inspeccion(models.Model):
    _name = 'upopark.mantenimiento.inspeccion'
    _description = 'Inspección de mantenimiento'
    _rec_name = 'strReferencia'
    _order = 'id desc'
    _sql_constraints = [
        ('reference_unique', 'UNIQUE("strReferencia")', 'La referencia de la inspección ya existe.'),
    ]

    strReferencia = fields.Char(string='Referencia', required=True, readonly=True, copy=False)
    m2oOrdenTrabajoId = fields.Many2one(
        'upopark.mantenimiento.orden_trabajo', string='Orden de trabajo',
        required=True, ondelete='restrict', index=True,
    )
    m2oIndisponibilidadId = fields.Many2one(
        'upopark.mantenimiento.indisponibilidad', string='Indisponibilidad documentada',
        ondelete='restrict', index=True,
    )
    m2oInspectorId = fields.Many2one(
        'res.partner', string='Persona que realiza la inspección', ondelete='restrict',
    )
    dateFechaInspeccion = fields.Date(string='Fecha de inspección')
    m2oResultadoId = fields.Many2one(
        'upopark.mantenimiento.resultado', string='Resultado general',
        ondelete='restrict',
    )
    strObservaciones = fields.Text(string='Observaciones')
    o2mPuntosComprobacionIds = fields.One2many(
        'upopark.mantenimiento.elemento_inspeccionado', 'm2oInspeccionId',
        string='Puntos de comprobación', copy=False,
    )

    @api.model_create_multi
    def create(self, lstValores):
        return super().create([
            dict(dictValores, strReferencia=self.env['ir.sequence'].next_by_code('upopark.mantenimiento.inspeccion'))
            for dictValores in lstValores
        ])

    @api.constrains('m2oInspectorId', 'dateFechaInspeccion', 'm2oResultadoId')
    def _comprobar_inspeccion_completada(self):
        for rsInspeccion in self:
            if rsInspeccion.m2oResultadoId and not (rsInspeccion.m2oInspectorId and rsInspeccion.dateFechaInspeccion):
                raise ValidationError('Indica quién realizó la inspección y en qué fecha antes de guardar su resultado.')
