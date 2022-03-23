# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class jugador(models.Model):
#     _name = 'jugador.jugador'
#     _description = 'jugador.jugador'

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
class echipo(models.Model):
    _name = 'jugador.equipo'
    _description = 'Define los atributos de un equipo'

    # Atributos
    nombreEchipo = fields.Char(string='Nombre equipo', required=True)

    #Relacion entre tablas
    jugador_id = fields.One2many('jugador.jugador','equipo_id', string='Equipo')

    def name_get(self):
        listaEquipo= []
        for equipo in self:
            listaEquipo.append((equipo.id, equipo.nombreEquipo))
        return listaEquipo
