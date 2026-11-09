from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Indisponibilidad(models.Model):
    _name = 'upopark.mantenimiento.indisponibilidad'
    _description = 'Indisponibilidad de un recurso'
    _rec_name = 'strReferencia'
    _rec_names_search = ['strReferencia', 'strMotivo']
    _order = 'dtInicio desc, id desc'
    _sql_constraints = [
        ('reference_unique', 'UNIQUE("strReferencia")', 'La referencia de la indisponibilidad ya existe.'),
    ]

    strReferencia = fields.Char(string='Referencia', required=True, readonly=True, copy=False)
    strMotivo = fields.Text(string='Motivo', required=True)
    m2oRecursoId = fields.Many2one(
        'upopark.recurso', string='Recurso', required=True,
        ondelete='restrict', index=True,
    )
    m2oIncidenciaId = fields.Many2one(
        'upopark.mantenimiento.incidencia', string='Incidencia',
        ondelete='restrict', index=True,
    )
    dtInicio = fields.Datetime(string='Inicio', required=True, default=fields.Datetime.now)
    dtFin = fields.Datetime(string='Fin')
    o2mInspeccionesIds = fields.One2many(
        'upopark.mantenimiento.inspeccion', 'm2oIndisponibilidadId',
        string='Inspecciones que la documentan', copy=False,
    )

    @api.depends('strReferencia')
    def _compute_display_name(self):
        for rsIndisponibilidad in self:
            rsIndisponibilidad.display_name = rsIndisponibilidad.strReferencia or 'Nueva indisponibilidad'

    @api.model_create_multi
    def create(self, lstValores):
        return super().create([
            dict(dictValores, strReferencia=self.env['ir.sequence'].next_by_code('upopark.mantenimiento.indisponibilidad'))
            for dictValores in lstValores
        ])

    @api.constrains('dtInicio', 'dtFin')
    def _comprobar_intervalo(self):
        for rsIndisponibilidad in self:
            if (rsIndisponibilidad.dtInicio and rsIndisponibilidad.dtFin
                    and rsIndisponibilidad.dtFin <= rsIndisponibilidad.dtInicio):
                raise ValidationError('El fin de la indisponibilidad debe ser posterior al inicio.')
