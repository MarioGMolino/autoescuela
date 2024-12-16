# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class autoescuela(models.Model):
#     _name = 'autoescuela.autoescuela'
#     _description = 'autoescuela.autoescuela'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class Autoescuela(models.Model):
    _name = 'Autoescuela'
    _description = "Modelo general de la autoescuela"
    name = fields.Char(string = 'Nombre', required = True)
    domicilio = fields.Char(string = 'Domicilio')
    localidad = fields.Char(string ='Localidad')
    provincia = fields.Char(string = 'Provincia')
    examen_ids = fields.Many2many('autoescuela.autoescuela', string='Examenes')
    profesor_ids = fields.One2Many('autoescuela.autoescuela','autoescuela_id', string='Profesor')
    alumno_ids = fields.One2Many('autoescuela.autoescuela', 'autoescuela_id', string='Alumno')
    contacto = fields.Char(string = 'Contacto')
    
    