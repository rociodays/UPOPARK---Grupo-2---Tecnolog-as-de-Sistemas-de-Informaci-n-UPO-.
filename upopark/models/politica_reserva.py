# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PoliticaReserva(models.Model):
    _name = 'upopark.politica_reserva'
    _description = 'Politica de Reserva'

    #atributos simples
    name = fields.Char(string='Codigo', required=True, help='Dame el codigo de la politica.')
    cNombre = fields.Char(string='Nombre', required=True, help='Dame el nombre de la politica.')
    iDiasAntelacion = fields.Integer(string='Dias de Antelacion', required=True, help='Dame el numero de dias de antelacion.')
    iDuracionMaxima = fields.Integer(string='Duracion Maxima', required=True, help='Dame la duracion maxima permitida.')
    iAntelacionCancel = fields.Integer(string='Antelacion Cancelacion', required=True, help='Dame los minutos de antelacion para cancelar la reserva.')

    #atributos complejos
    reserva_ids = fields.One2many('upopark.reserva','politica_reserva_id','Reservas Vinculadas')

    #sql constraints
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'El codigo de la politica ya esta registrado.'),
    ]

    #validaciones
    #nombre longitud
    @api.constrains('cNombre')
    def _check_longitud_nombre(self):
        for record in self:
            if record.cNombre:
                if len(record.cNombre) < 3 or len(record.cNombre) > 100:
                    raise ValidationError('El nombre de la politica debe tener entre 3 y 100 caracteres.')

    #rangos numeros
    @api.onchange('iDuracionMaxima', 'iDiasAntelacion', 'iAntelacionCancel')
    def _onchange_ajustar_valores_numericos(self):
        resultado = {}
        mensajes = []
        
        if self.iDuracionMaxima and self.iDuracionMaxima < 1:
            self.iDuracionMaxima = 1
            mensajes.append('La duracion maxima no pude ser negativa.')
            
        if self.iDiasAntelacion and self.iDiasAntelacion < 0:
            self.iDiasAntelacion = 0
            mensajes.append('Los dias de antelacion no pueden ser negativos.')
            
        if self.iAntelacionCancel and self.iAntelacionCancel < 0:
            self.iAntelacionCancel = 0
            mensajes.append('La antelacion de cancelacion no puede ser negativa.')

        if mensajes:
            resultado = {
                'warning': {
                    'title': 'Errores de politica',
                    'message': ' '.join(mensajes)
                }
            }
            return resultado