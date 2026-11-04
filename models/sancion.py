# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Sancion(models.Model):
    _name = 'upopark.sancion'
    _description = 'Sanción'
    _rec_name = 'tipo_sancion_id'

    dfechainicio = fields.Date(string='Fecha Inicio')
    dfechafin = fields.Date(string='Fecha Fin')
    smotivos = fields.Text(string='Motivos')
    tipo_sancion_id = fields.Many2one(
        'upopark.tipo_sancion', string='Tipo de Sanción', required=True,
        ondelete='restrict',
    )
    sestado = fields.Selection(
        [('pendiente', 'Pendiente'), ('activa', 'Activa'),
         ('cumplida', 'Cumplida'), ('anulada', 'Anulada')],
        string='Estado', default='pendiente', required=True,
    )

    @api.constrains('dfechainicio', 'dfechafin')
    def _check_fechas_sancion(self):
        for record in self:
            if (record.dfechainicio and record.dfechafin
                    and record.dfechafin < record.dfechainicio):
                raise ValidationError('La fecha de fin de la sanción no puede ser anterior a la fecha de inicio.')

    def btn_activar_sancion(self):
        for record in self:
            if record.sestado != 'pendiente':
                raise ValidationError('Solo se pueden activar sanciones pendientes.')
            record.write({'sestado': 'activa'})

    def btn_cumplir_sancion(self):
        for record in self:
            if record.sestado != 'activa':
                raise ValidationError('Solo se pueden cumplir sanciones activas.')
            record.write({'sestado': 'cumplida'})

    def btn_anular_sancion(self):
        for record in self:
            if record.sestado not in ('pendiente', 'activa'):
                raise ValidationError('Solo se pueden anular sanciones pendientes o activas.')
            record.write({'sestado': 'anulada'})
