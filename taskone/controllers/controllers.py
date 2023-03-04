# -*- coding: utf-8 -*-
# from odoo import http


# class C:\users\mmsi\desktop\modules\taskone(http.Controller):
#     @http.route('/c:\users\mmsi\desktop\modules\taskone/c:\users\mmsi\desktop\modules\taskone', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\users\mmsi\desktop\modules\taskone/c:\users\mmsi\desktop\modules\taskone/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\users\mmsi\desktop\modules\taskone.listing', {
#             'root': '/c:\users\mmsi\desktop\modules\taskone/c:\users\mmsi\desktop\modules\taskone',
#             'objects': http.request.env['c:\users\mmsi\desktop\modules\taskone.c:\users\mmsi\desktop\modules\taskone'].search([]),
#         })

#     @http.route('/c:\users\mmsi\desktop\modules\taskone/c:\users\mmsi\desktop\modules\taskone/objects/<model("c:\users\mmsi\desktop\modules\taskone.c:\users\mmsi\desktop\modules\taskone"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\users\mmsi\desktop\modules\taskone.object', {
#             'object': obj
#         })
