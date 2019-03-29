# -*- coding: utf-8 -*-
from odoo import http

# class DirectoriOdoo/odoo/addons/myconferences(http.Controller):
#     @http.route('/directori_odoo/odoo/addons/myconferences/directori_odoo/odoo/addons/myconferences/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/directori_odoo/odoo/addons/myconferences/directori_odoo/odoo/addons/myconferences/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('directori_odoo/odoo/addons/myconferences.listing', {
#             'root': '/directori_odoo/odoo/addons/myconferences/directori_odoo/odoo/addons/myconferences',
#             'objects': http.request.env['directori_odoo/odoo/addons/myconferences.directori_odoo/odoo/addons/myconferences'].search([]),
#         })

#     @http.route('/directori_odoo/odoo/addons/myconferences/directori_odoo/odoo/addons/myconferences/objects/<model("directori_odoo/odoo/addons/myconferences.directori_odoo/odoo/addons/myconferences"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('directori_odoo/odoo/addons/myconferences.object', {
#             'object': obj
#         })