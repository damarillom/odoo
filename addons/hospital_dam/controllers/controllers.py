# -*- coding: utf-8 -*-
from odoo import http

# class HospitalDam(http.Controller):
#     @http.route('/hospital_dam/hospital_dam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_dam/hospital_dam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_dam.listing', {
#             'root': '/hospital_dam/hospital_dam',
#             'objects': http.request.env['hospital_dam.hospital_dam'].search([]),
#         })

#     @http.route('/hospital_dam/hospital_dam/objects/<model("hospital_dam.hospital_dam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_dam.object', {
#             'object': obj
#         })