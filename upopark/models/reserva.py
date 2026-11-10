# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Reserva(models.Model):
    _name = 'upopark.reserva'
    _description = 'Reserva de Parking'

    #atributos simples
    name = fields.Char(string="Referencia", required=True, help="Dame la referencia de la reserva.")
    fInicio = fields.Datetime('Inicio', required=True, autodate = True, help="Dame la fecha de inicio de la reserva.")
    fFin = fields.Datetime('Fin', required=True, autodate = True, help="Dame la fecha de fin de la reserva.")

    #atributos complejos
    vehiculo_id = fields.Many2one('upopark.vehiculo',string='Vehículo',required=True,help='Dame el vehiculo para esta reserva.')
    estado_reserva_id = fields.Many2one('upopark.estado_reserva',string='Estado Actual',required=True,help='Dame el estado actual de la reserva.')
    politica_reserva_id = fields.Many2one('upopark.politica_reserva',string='Política Aplicada',required=True,help='Dame la politica aplicada a esta reserva.')
    
    historial_ids = fields.One2many('upopark.historial_reserva','reserva_id','Historial de Cambios')
    cancelacion_ids = fields.One2many('upopark.cancelacion_reserva','reserva_id','Registros de Cancelación')
    
    #sql constraints
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'La referencia de la reserva ya esta registrada.')
    ]

    #validaciones
    #referencia
    @api.constrains('name')
    def _check_formato_referencia(self):
        for record in self:
            if record.name:
                # Exige el formato RES-YYYY-XXXX (ej. RES-2026-0015)
                if not re.match(r'^RES-\d{4}-\d{3,6}$', record.name):
                    raise models.ValidationError('La referencia debe seguir el formato RES-YYYY-XXXX (ej. RES-2026-001).')

    #fecha inicio
    @api.onchange('fInicio')
    def _onchange_fecha_inicio_reserva(self):
        if self.fInicio:
            ahora = fields.Datetime.now()
            if self.fInicio < ahora:
                self.fInicio = ahora
                raise models.ValidationError('No puedes crear una reserva en el pasado.')

    #rangos de fechas y duracion maxima
    @api.constrains('fInicio', 'fFin', 'politica_reserva_id')
    def _check_logica_fechas_y_politica(self):
        for record in self:
            if record.fInicio and record.fFin:
                if record.fFin <= record.fInicio:
                    raise models.ValidationError('La fecha de fin debe ser posterior a la de inicio.')
                
                if record.politica_reserva_id and record.politica_reserva_id.iDuracionMaxima:
                    diferencia = record.fFin - record.fInicio
                    if diferencia.days > record.politica_reserva_id.iDuracionMaxima:
                        raise models.ValidationError(f'La reserva de {diferencia.days} dias excede el limite de '
                            f'{record.politica_reserva_id.iDuracionMaxima} dias establecido en su politica.'
                        )
