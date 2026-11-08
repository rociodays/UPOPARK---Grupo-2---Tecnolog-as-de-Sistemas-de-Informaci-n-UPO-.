# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class EventoCampus(models.Model):
    _name = 'upopark.evento_campus'
    _description = 'Evento Campus'
    _rec_name = 'snombre'

    snombre = fields.Char(string='Nombre', required=True)
    dtfechainicio = fields.Datetime(string='Fecha Inicio', required=True)
    dtfechafin = fields.Datetime(string='Fecha Fin', required=True)
    @api.onchange('dtfechainicio')
    def _onchange_fecha_inicio(self):
        if self.dtfechainicio:
            self.dtfechafin = self.dtfechainicio + timedelta(hours=2)

    @api.constrains('dtfechainicio', 'dtfechafin')
    def _check_fechas(self):
        for record in self:
            if (record.dtfechainicio and record.dtfechafin
                    and record.dtfechafin <= record.dtfechainicio):
                raise ValidationError('La fecha de fin debe ser posterior a la fecha de inicio del evento.')
