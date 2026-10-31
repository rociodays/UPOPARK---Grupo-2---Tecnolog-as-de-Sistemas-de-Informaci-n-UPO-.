# from odoo import http


# class Upopark(http.Controller):
#     @http.route('/upopark/upopark', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upopark/upopark/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('upopark.listing', {
#             'root': '/upopark/upopark',
#             'objects': http.request.env['upopark.upopark'].search([]),
#         })

#     @http.route('/upopark/upopark/objects/<model("upopark.upopark"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upopark.object', {
#             'object': obj
#         })

