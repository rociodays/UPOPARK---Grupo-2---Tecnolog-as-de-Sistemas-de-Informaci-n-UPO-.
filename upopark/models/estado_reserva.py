# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import ValidationError

class EstadoReserva(models.Model):
    _name = 'upopark.estado_reserva'
    _description = 'Estados de Reserva'

    #atributos simples    
    name = fields.Selection(
            [('borrador', 'Borrador'),
            ('confirmada', 'Confirmada'),
            ('activa', 'Activa'),
            ('finalizada', 'Finalizada'),
            ('cancelada', 'Cancelada')], string='Estado Reserva', required=True)
    
    cDescripcion = fields.Text(string='Descripcion')

    #atributos complejos
    reserva_ids = fields.One2many('upopark.reserva','estado_reserva_id','Reservas en este Estado')

    #sql constraints
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'El estado de reserva ya esta registrado.')
    ]

    #validaciones
    #descripcion
    @api.constrains('cDescripcion')
    def _check_longitud_descripcion_estado(self):
        for record in self:
            if record.cDescripcion:
                if len(record.cDescripcion) < 5 or len(record.cDescripcion) > 250:
                    raise ValidationError('La descripcion del estado debe tener entre 5 y 250 caracteres.')
