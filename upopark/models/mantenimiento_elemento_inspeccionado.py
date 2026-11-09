from odoo import fields, models


class ElementoInspeccionado(models.Model):
    _name = 'upopark.mantenimiento.elemento_inspeccionado'
    _description = 'Elemento inspeccionado'
    _rec_name = 'strNombre'
    _order = 'iSecuencia, id'

    m2oInspeccionId = fields.Many2one(
        'upopark.mantenimiento.inspeccion', string='Inspección',
        required=True, ondelete='cascade', index=True,
    )
    strNombre = fields.Char(string='Punto de comprobación', required=True)
    iSecuencia = fields.Integer(string='Secuencia', default=10)
    selResultado = fields.Selection(
        [('pending', 'Pendiente'), ('passed', 'Conforme'), ('failed', 'No conforme')],
        string='Resultado', default='pending', required=True,
    )
