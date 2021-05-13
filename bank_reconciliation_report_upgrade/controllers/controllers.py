# -*- coding: utf-8 -*-
# from odoo import http


# class BankReconciliationReportUpgrade(http.Controller):
#     @http.route('/bank_reconciliation_report_upgrade/bank_reconciliation_report_upgrade/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bank_reconciliation_report_upgrade/bank_reconciliation_report_upgrade/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bank_reconciliation_report_upgrade.listing', {
#             'root': '/bank_reconciliation_report_upgrade/bank_reconciliation_report_upgrade',
#             'objects': http.request.env['bank_reconciliation_report_upgrade.bank_reconciliation_report_upgrade'].search([]),
#         })

#     @http.route('/bank_reconciliation_report_upgrade/bank_reconciliation_report_upgrade/objects/<model("bank_reconciliation_report_upgrade.bank_reconciliation_report_upgrade"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bank_reconciliation_report_upgrade.object', {
#             'object': obj
#         })
