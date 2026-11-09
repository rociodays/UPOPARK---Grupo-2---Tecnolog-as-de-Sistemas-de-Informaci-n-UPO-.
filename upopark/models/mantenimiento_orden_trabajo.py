from odoo import api, fields, models


class OrdenTrabajo(models.Model):
    _name = 'upopark.mantenimiento.orden_trabajo'
    _description = 'Orden de trabajo'
    _rec_name = 'strReferencia'
    _order = 'dtInicioPrevisto desc, id desc'
    _sql_constraints = [
        ('reference_unique', 'UNIQUE("strReferencia")', 'La referencia de la orden ya existe.'),
    ]

    strReferencia = fields.Char(string='Referencia', required=True, readonly=True, copy=False)
    strAsunto = fields.Char(string='Asunto', required=True)
    dtInicioPrevisto = fields.Datetime(string='Inicio previsto')
    m2oIncidenciaId = fields.Many2one(
        'upopark.mantenimiento.incidencia', string='Incidencia', ondelete='restrict', index=True,
    )
    m2oResponsableId = fields.Many2one(
        'res.partner', string='Responsable', required=True, ondelete='restrict',
    )
    o2mTareasIds = fields.One2many(
        'upopark.mantenimiento.tarea', 'm2oOrdenTrabajoId', string='Tareas', copy=False,
    )
    o2mInspeccionesIds = fields.One2many(
        'upopark.mantenimiento.inspeccion', 'm2oOrdenTrabajoId', string='Inspecciones', copy=False,
    )

    @api.model_create_multi
    def create(self, lstValores):
        return super().create([
            dict(dictValores, strReferencia=self.env['ir.sequence'].next_by_code('upopark.mantenimiento.orden_trabajo'))
            for dictValores in lstValores
        ])
