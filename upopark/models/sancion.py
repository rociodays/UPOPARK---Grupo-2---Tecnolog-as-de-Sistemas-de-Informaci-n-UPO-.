from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Sancion(models.Model):
    _name = 'upopark.sancion'
    _description = 'Sanción'
    _rec_name = 'tipo_sancion_id'

    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_fin = fields.Date(string='Fecha Fin')
    motivos = fields.Text(string='Motivos')
    estado = fields.Selection([('pendiente', 'Pendiente'), ('activa', 'Activa'), ('cumplida', 'Cumplida'), ('anulada', 'Anulada')],
        string='Estado', default='pendiente', required=True,
    )
    tipo_sancion_id = fields.Many2one('upopark.tipo_sancion', string='Tipo de Sanción', required=True, ondelete='restrict')
    contacto_id = fields.Many2one('upopark.contacto', string='Contacto sancionado')

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas_sancion(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin and record.fecha_fin < record.fecha_inicio:
                raise ValidationError('La fecha de fin de la sanción no puede ser anterior a la fecha de inicio.')

    def btn_activar_sancion(self):
        for record in self:
            if record.estado != 'pendiente':
                raise ValidationError('Solo se pueden activar sanciones pendientes.')
            record.write({'estado': 'activa'})

    def btn_cumplir_sancion(self):
        for record in self:
            if record.estado != 'activa':
                raise ValidationError('Solo se pueden cumplir sanciones activas.')
            record.write({'estado': 'cumplida'})

    def btn_anular_sancion(self):
        for record in self:
            if record.estado not in ('pendiente', 'activa'):
                raise ValidationError('Solo se pueden anular sanciones pendientes o activas.')
            record.write({'estado': 'anulada'})