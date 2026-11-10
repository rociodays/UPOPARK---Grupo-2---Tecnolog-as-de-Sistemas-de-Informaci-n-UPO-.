# -*- coding: utf-8 -*-

from odoo import models, fields

class EstadoReserva(models.Model):
    _name = 'upopark.estado_reserva'
    _description = 'Estados de Reserva'

    name = fields.Selection(
            [('borrador', 'Borrador'),
            ('confirmada', 'Confirmada'),
            ('activa', 'Activa'),
            ('finalizada', 'Finalizada'),
            ('cancelada', 'Cancelada')], string='Estado Reserva', required=True)
    
    cDescripcion = fields.Text(string='Descripcion')