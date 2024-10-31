# -*- coding: utf-8 -*-
# from odoo import http


# class TechnicalTestTunas(http.Controller):
#     @http.route('/technical_test_tunas/technical_test_tunas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/technical_test_tunas/technical_test_tunas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('technical_test_tunas.listing', {
#             'root': '/technical_test_tunas/technical_test_tunas',
#             'objects': http.request.env['technical_test_tunas.technical_test_tunas'].search([]),
#         })

#     @http.route('/technical_test_tunas/technical_test_tunas/objects/<model("technical_test_tunas.technical_test_tunas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('technical_test_tunas.object', {
#             'object': obj
#         })
