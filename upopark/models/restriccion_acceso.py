# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RestriccionAcceso(models.Model):
    _name = 'upopark.restriccion_acceso'
    _description = 'Restriccion de Acceso'

    #atributos simples
    name = fields.Char(string="Matricula", required=True, help="Dame la matrícula del vehiculo.")
    fInicio = fields.Datetime('Inicio', required=True, autodate = True, help="Dame la fecha de inicio de la restriccion.")
    fFin = fields.Datetime('Fin', required=True, autodate = True, help="Dame la fecha de fin de la restriccion.")
    bActivo = fields.Boolean('Activa',compute='_compute_bActivo')

    #atributos complejos
    vehiculo_id = fields.Many2one('upopark.vehiculo',string='Vehículo',required=True,help='Dame el vehículo al que se le aplica la restriccion.')
    motivo_restriccion_id = fields.Many2one('upopark.motivo_restriccion', string='Motivo de Restricción',required=True, help='Dame el motivo de la restriccion.')

    #sql constraints no tiene

    #metodo bActivo
    @api.depends('fInicio', 'fFin')
    def _compute_bActivo(self):
        for record in self:
            if record.fInicio and record.fFin:
                current_time = fields.Datetime.now()
                if record.fInicio <= current_time <= record.fFin:
                    record.bActivo = True
                else:
                    record.bActivo = False
            else:
                record.bActivo = False

    #validaciones
    #fecha inicio
    @api.onchange('fInicio')
    def _onchange_fecha_inicio(self):
        if self.fInicio:
            ahora = fields.Datetime.now()
            # Si la fecha introducida es anterior a este mismo instante, es un error
            if self.fInicio < ahora:
                self.fInicio = ahora
                raise models.ValidationError('La restriccion no puede empezar en el pasado.')

    #fecha final
    @api.constrains('fInicio', 'fFin')
    def _check_rango_fechas(self):
        for record in self:
            if record.fInicio and record.fFin:
                if record.fFin < record.fInicio:
                    raise models.ValidationError('La fecha de finalizacion no puede ser anterior a la fecha de inicio.')