from odoo import api, fields, models


class PlanPreventivo(models.Model):
    _name = 'upopark.plan_preventivo'
    _description = 'Plan preventivo de un recurso'
    _rec_name = 'strCodigo'
    _rec_names_search = ['strCodigo', 'strDescripcion']
    _order = 'strCodigo'
    _sql_constraints = [
        ('codigo_unique', 'UNIQUE("strCodigo")', 'El código del plan preventivo ya existe.'),
    ]

    strCodigo = fields.Char(string='Código', required=True, copy=False)
    strDescripcion = fields.Text(string='Descripción')
    recurso_id = fields.Many2one(
        'upopark.recurso', string='Recurso', required=True,
        ondelete='restrict', index=True,
    )

    @api.depends('strCodigo')
    def _compute_display_name(self):
        for rsPlan in self:
            rsPlan.display_name = rsPlan.strCodigo or 'Nuevo plan preventivo'
