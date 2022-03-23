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

class equipo(models.Model):
    _name = 'jugador.equipo'
    _description = 'Define los atributos de un equipo'

    # Atributos
    nombreEquipo = fields.Char(string='Nombre equipo', required=True)

    #Relacion entre tablas
    empleado_id = fields.One2many('jugador.empleado','equipo_id', string='Equipo')

    def name_get(self):
        listaEquipos = []
        for equipo in self:
            listaEquipos.append((equipo.id, equipo.nombreEquipo))
        return listaEquipos

class empleado(models.Model):
    _name = 'jugador.empleado'
    _description = 'Define los atributos de un empleado'

    # Atributos
    dniEmpleado = fields.Char(string='DNI', required=True)
    nombreEmpleado = fields.Char(string='Nombre y apellidos', required=True)
    fechaNacimiento = fields.Date(string='Fecha Nacimiento', required=True, default = fields.date.today())
    direccionEmpleado = fields.Char(string='Direccon')
    telefonoEmpleado = fields.Char(string='Telefono')
    edad = fields.Integer('Edad', compute='_getEdad')

    #Relacion de tablas
    equipo_id = fields.Many2one('jugador.equipo', string='Equipo')
    competicia_ids = fields.Many2many('jugador.competicia', string='Competicias')


    @api.depends('fechaNacimiento')
    def _getEdad(self):
        hoy = date.today()
        for empleado in self:
            empleado.edad = relativedelta(hoy, empleado.fechaNacimiento).years

    @api.constrains('fechaNacimiento')
    def _checkEdad(self):
        for empleado in self:
            if (empleado.edad < 18):
                raise exceptions.ValidationError("El empleado no puede ser menor de edad")
    
    @api.constrains('dniEmpleado')
    def _checkDNI(self):
        for empleado in self:
            if (len(empleado.dniEmpleado) > 9):
                raise exceptions.ValidationError("El DNI no puede tener mas 9 caracteres")
            if (len(empleado.dniEmpleado) < 9):
                raise exceptions.ValidationError("El DNI no puede tener menos 9 caracteres")

class competicia(models.Model):
     _name = 'jugador.competicia'
     _description = 'Define los atributos de un competicia'

     #Atributos
     nombreCompeticia = fields.Char(string='Nombre competicia', required=True)
     tipoCompeticia = fields.Selection(string='Tipo de competicia', selection=[('n','Nacional'),('i','Internacional')], help='Tipo de competicia al que se esta destinando' )
     descripcionCompeticia = fields.Text(string='Descripcion del competicia')
     fechaInicio = fields.Date(string='Fecha de Inicio', required=True)
     fechaFin = fields.Date(string='Fecha de fin', required=True)
     #dias = fields.Integer(string='Dias')
     #Relacion entre tablas
     empleado_id = fields.Many2many('jugador.empleado', string='Empleados')

     @api.constrains('fechaFin')
     def _checkFechaFin(self):
         for competicia in self:
             if relativedelta(competicia.fechaInicio, competicia.fechaFin).days > 0:
                 raise exceptions.ValidationError("La fecha de fin no puede ser inferior a la fecha de inicio")
     
     @api.constrains('fechaInicio')
     def _checkFechaInicio(self):
         hoy = date.today()
         for competicia in self:
             diasCalculados = relativedelta(hoy, competicia.fechaInicio).days
             if ( diasCalculados > 0):
                 raise exceptions.ValidationError("La fecha no puede ser anterior a la fecha actual")

     

