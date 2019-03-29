# -*- coding: utf-8 -*-
from odoo import http

class tasquescbm(http.Controller):
     @http.route('/tasquescbm/', auth='public')
     def index(self, **kw):
         return "Hello, world"

#     @http.route('/todo_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/todo_task.listing', {
#             'root': '//todo_task/todo_task,
#             'objects': http.request.env['/todo_task.todo_task'].search([]),
#         })

#     @http.route('//home/carlota/odoo/addons/tasquescbm//home/carlota/odoo/addons/tasquescbm/objects/<model("/home/carlota/odoo/addons/tasquescbm./home/carlota/odoo/addons/tasquescbm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/carlota/odoo/addons/tasquescbm.object', {
#             'object': obj
#         })
