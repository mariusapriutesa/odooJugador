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
        
class jugador(models.Model):
    _name = 'jugador.jugador'
    _description = 'Define los atributos de un jugador'

    # Atributos
    dniJugador = fields.Char(string='DNI', required=True)
    nombreJugador = fields.Char(string='Nombre y apellidos', required=True)
    fechaNacimiento = fields.Date(string='Fecha Nacimiento', required=True, default = fields.date.today())
    direccionJugador = fields.Char(string='Direccon')
    telefonoJugador = fields.Char(string='Telefono')
    edad = fields.Integer('Edad', compute='_getEdad')

    #Relacion de tablas
    echipo_id = fields.Many2one('jugador.echipo', string='Echipo')
    jugadores_ids = fields.Many2many('jugador.jugadores', string='Jugador')


    @api.depends('fechaNacimiento')
    def _getEdad(self):
        hoy = date.today()
        for jugador in self:
            jugador.edad = relativedelta(hoy, jugador.fechaNacimiento).years

    @api.constrains('fechaNacimiento')
    def _checkEdad(self):
        for jugador in self:
            if (jugador.edad < 18):
                raise exceptions.ValidationError("El jugador no puede ser menor de edad")
    
    @api.constrains('dniJugador')
    def _checkDNI(self):
        for jugador in self:
            if (len(jugador.dniJugador) > 9):
                raise exceptions.ValidationError("El DNI no puede tener mas 9 caracteres")
            if (len(jugador.dniJugador) < 9):
                raise exceptions.ValidationError("El DNI no puede tener menos 9 caracteres")

