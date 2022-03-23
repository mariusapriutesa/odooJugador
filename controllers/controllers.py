# -*- coding: utf-8 -*-
# from odoo import http


# class Jugador(http.Controller):
#     @http.route('/jugador/jugador/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jugador/jugador/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jugador.listing', {
#             'root': '/jugador/jugador',
#             'objects': http.request.env['jugador.jugador'].search([]),
#         })

#     @http.route('/jugador/jugador/objects/<model("jugador.jugador"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jugador.object', {
#             'object': obj
#         })
