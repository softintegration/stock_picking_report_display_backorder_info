# -*- coding: utf-8 -*- 


{
    'name': 'Display backorder informations in the main delivery printed document',
    'author': 'Soft-integration',
    'application': True,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Stock',
    'demo': [],
    'depends': ['stock'],
    'data': [
        'report/report_deliveryslip.xml',
        'views/stock_picking_views.xml'
    ],
    'license': 'LGPL-3',
}
