# -*- coding: utf-8 -*-
from odoo import http

# class VitDinamicSequence(http.Controller):
#     @http.route('/vit_dinamic_sequence/vit_dinamic_sequence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_dinamic_sequence/vit_dinamic_sequence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_dinamic_sequence.listing', {
#             'root': '/vit_dinamic_sequence/vit_dinamic_sequence',
#             'objects': http.request.env['vit_dinamic_sequence.vit_dinamic_sequence'].search([]),
#         })

#     @http.route('/vit_dinamic_sequence/vit_dinamic_sequence/objects/<model("vit_dinamic_sequence.vit_dinamic_sequence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_dinamic_sequence.object', {
#             'object': obj
#         })