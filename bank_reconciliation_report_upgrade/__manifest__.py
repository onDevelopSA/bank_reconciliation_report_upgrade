# -*- coding: utf-8 -*-
# © 2021 onDevelop.sa
# Autor: Idelis Gé Ramírez
# Part of onDevelop.SA. See LICENSE file for full copyright and licensing details.

{
    'name': "Bank Reconciliation Report Upgrade",
    'summary': """Add the Partner Name column in the bank reconciliation report.""",
    'description': """
    Add the Partner Name column in the bank reconciliation report.
    """,
    'author': "onDevelop.SA",
    'website': "http://www.ondevelop.tech",
    'category': 'Accounting/Accounting',
    'version': '14.0.1',
    'license': 'LGPL-3',
    'price': 14,
    'currency': 'USD',
    'support': "ondevelop.sa@gmail.com",
    'depends': ['base', 'account_reports'],
    'images': ['static/description/partner_column_cover.png'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False
}
