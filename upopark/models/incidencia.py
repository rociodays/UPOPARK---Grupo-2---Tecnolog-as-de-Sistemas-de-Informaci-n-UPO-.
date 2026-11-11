from odoo import api, fields, models


class Incidencia(models.Model):
    _name = 'upopark.incidencia'
    _description = 'Incidencia'
    _rec_name = 'strReferencia'
    _rec_names_search = ['strReferencia', 'strAsunto']
    _order = 'id desc'
    _sql_constraints = [
        ('reference_unique', 'UNIQUE("strReferencia")', 'La referencia de incidencia ya existe.'),
    ]

    strReferencia = fields.Char(string='Referencia', required=True, readonly=True, copy=False)
    strAsunto = fields.Char(string='Asunto', required=True)
    strDescripcion = fields.Text(string='Descripción')
    tipo_incidencia_id = fields.Many2one(
        'upopark.tipo_incidencia', string='Tipo',
        required=True, ondelete='restrict', index=True,
    )
    estado_incidencia_id = fields.Many2one(
        'upopark.estado_incidencia', string='Estado',
        required=True, ondelete='restrict', index=True,
    )
    contacto_reporta_id = fields.Many2one(
        'res.partner', string='Contacto que reporta', required=True, ondelete='restrict',
    )
    orden_trabajo_ids = fields.One2many(
        'upopark.orden_trabajo', 'incidencia_id', string='Órdenes de trabajo',
    )
    indisponibilidad_ids = fields.One2many(
        'upopark.indisponibilidad', 'incidencia_id',
        string='Indisponibilidades', copy=False,
    )

    @api.depends('strReferencia', 'strAsunto')
    def _compute_display_name(self):
        for rsIncidencia in self:
            lstPartes = [
                strParte for strParte in (rsIncidencia.strReferencia, rsIncidencia.strAsunto)
                if strParte
            ]
            rsIncidencia.display_name = ' · '.join(lstPartes) or 'Nueva incidencia'

    @api.model_create_multi
    def create(self, lstValores):
        return super().create([
            dict(dictValores, strReferencia=self.env['ir.sequence'].next_by_code('upopark.incidencia'))
            for dictValores in lstValores
        ])
