from odoo import models, fields, api

class ResolucionAlegacion(models.Model):
    _name = 'upopark.resolucion_alegacion'
    _descripcion = 'Resolución de Alegación'

    fecha_resolucion = fields.Datetime(string='Fecha de resolucion', required=True)
    dictamen_final = fields.Selection(
        [('estimada','Estimada (Multa anulada)'), ('desestimada', 'Desestimada (Multa mantenida)')],
        string="Dictamen final", required=True, default='desestimada')
    administrador_responsable = fields.Char(string='Administrador responsable', required=True)

    alegacion_id = fields.Many2one('upopark.alegacion', string='Alegacion', required=True)