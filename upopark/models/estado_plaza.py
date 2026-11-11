from odoo import models, fields, api

class EstadoPlaza(models.Model):
    
    _name = 'upopark.estado_plaza'
    _description = 'Estado de una plaza'

    estado = fields.Char('Estado', size=9, required=True)

    estadoPlaza_plaza = fields.One2many('upopark.plaza', 'EstadoPlaza muestra estado de Plaza') #odoo ya no acepta Many2one
