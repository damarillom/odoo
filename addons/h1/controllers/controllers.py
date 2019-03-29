# -*- coding: utf-8 -*-
from odoo import http

# class /home/carlota/odoo/addons/hospital(http.Controller):
#     @http.route('//home/carlota/odoo/addons/hospital//home/carlota/odoo/addons/hospital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/carlota/odoo/addons/hospital//home/carlota/odoo/addons/hospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/carlota/odoo/addons/hospital.listing', {
#             'root': '//home/carlota/odoo/addons/hospital//home/carlota/odoo/addons/hospital',
#             'objects': http.request.env['/home/carlota/odoo/addons/hospital./home/carlota/odoo/addons/hospital'].search([]),
#         })

#     @http.route('//home/carlota/odoo/addons/hospital//home/carlota/odoo/addons/hospital/objects/<model("/home/carlota/odoo/addons/hospital./home/carlota/odoo/addons/hospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/carlota/odoo/addons/hospital.object', {
#             'object': obj
#         })