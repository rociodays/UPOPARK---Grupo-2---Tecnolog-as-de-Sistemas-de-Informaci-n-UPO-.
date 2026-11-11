from odoo import models, fields, api

class CancelacionReserva(models.Model):
    _name = 'upopark.cancelacion_reserva'
    _description = 'Cancelacion de Reserva'
    
    
    #atributos simples
    fFechaCancelacion = fields.Datetime('Fecha de Cancelacion', required=True, autodate = True, help="Dame la fecha de cancelacion de la reserva.")
    cNota = fields.Text(string='Nota', help='Observaciones sobre el motivo del cambio de estado.')

    #atributos complejos
    name = fields.Many2one('upopark.reserva',string='Referencia Reserva',required=True,help='Dame la reserva que se ha cancelado.')
    usuario_id = fields.Many2one('upopark.usuario',string='Usuario',required=True,help='Dame el usuario que realiza la cancelacion.')

    #sql constraints
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Esta reserva ya ha sido cancelada.')
    ]

    #validaciones
    #fecha cancelacion
    @api.onchange('fFechaCancelacion')
    def _onchange_fecha_cancelacion(self):
        if self.fFechaCancelacion:
            ahora = fields.Datetime.now()
            if self.fFechaCancelacion > ahora:
                self.fFechaCancelacion = ahora
                raise models.ValidationError('No puedes registrar una cancelacion en el futuro.')

    #nota
    @api.constrains('cNota')
    def _check_nota_cancelacion(self):
        for record in self:
            if not record.cNota or len(record.cNota.strip()) < 10:
                raise models.ValidationError('La nota debe tener al menos 10 caracteres.')