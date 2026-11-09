from odoo import fields, models


class TareaMantenimiento(models.Model):
    _name = 'upopark.mantenimiento.tarea'
    _description = 'Tarea de mantenimiento'
    _rec_name = 'strNombre'
    _order = 'iSecuencia, id'

    m2oOrdenTrabajoId = fields.Many2one(
        'upopark.mantenimiento.orden_trabajo', string='Orden de trabajo', required=True,
        ondelete='cascade', index=True,
    )
    strNombre = fields.Char(string='Tarea', required=True)
    iSecuencia = fields.Integer(string='Secuencia', default=10)
