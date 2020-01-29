# -*- coding: utf-8 -*-
from odoo import http

# class Addons/gastosFondosxrendir(http.Controller):
#     @http.route('/addons/gastos_fondosxrendir/addons/gastos_fondosxrendir/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/gastos_fondosxrendir/addons/gastos_fondosxrendir/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/gastos_fondosxrendir.listing', {
#             'root': '/addons/gastos_fondosxrendir/addons/gastos_fondosxrendir',
#             'objects': http.request.env['addons/gastos_fondosxrendir.addons/gastos_fondosxrendir'].search([]),
#         })

#     @http.route('/addons/gastos_fondosxrendir/addons/gastos_fondosxrendir/objects/<model("addons/gastos_fondosxrendir.addons/gastos_fondosxrendir"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/gastos_fondosxrendir.object', {
#             'object': obj
#         })