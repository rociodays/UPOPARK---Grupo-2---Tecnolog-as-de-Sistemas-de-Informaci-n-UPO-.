from odoo import fields, models


class TipoIncidencia(models.Model):
    _name = 'upopark.mantenimiento.tipo_incidencia'
    _description = 'Tipo de incidencia'
    _rec_name = 'strNombre'
    _order = 'strNombre, id'
    _sql_constraints = [
        ('name_unique', 'UNIQUE("strNombre")', 'Ya existe una entrada con ese nombre.'),
    ]

    strNombre = fields.Char(string='Nombre', required=True)
    strDescripcion = fields.Text(string='Descripción')
