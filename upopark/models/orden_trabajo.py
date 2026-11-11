from odoo import api, fields, models


class OrdenTrabajo(models.Model):
    _name = 'upopark.orden_trabajo'
    _description = 'Orden de trabajo'
    _rec_name = 'strReferencia'
    _order = 'dtInicioPrevisto desc, id desc'
    _sql_constraints = [
        ('reference_unique', 'UNIQUE("strReferencia")', 'La referencia de la orden ya existe.'),
    ]

    strReferencia = fields.Char(string='Referencia', required=True, readonly=True, copy=False)
    strAsunto = fields.Char(string='Asunto', required=True)
    dtInicioPrevisto = fields.Datetime(string='Inicio previsto')
    incidencia_id = fields.Many2one(
        'upopark.incidencia', string='Incidencia', ondelete='restrict', index=True,
    )
    responsable_id = fields.Many2one(
        'res.partner', string='Responsable', required=True, ondelete='restrict',
    )
    tarea_ids = fields.One2many(
        'upopark.tarea', 'orden_trabajo_id', string='Tareas', copy=False,
    )
    inspeccion_ids = fields.One2many(
        'upopark.inspeccion', 'orden_trabajo_id', string='Inspecciones', copy=False,
    )

    @api.model_create_multi
    def create(self, lstValores):
        return super().create([
            dict(dictValores, strReferencia=self.env['ir.sequence'].next_by_code('upopark.orden_trabajo'))
            for dictValores in lstValores
        ])
