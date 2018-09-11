# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Duration Filter',
    'category': 'sale',
    'version': '11.0.1.0.0',
    'summary': 'This module manages the filtering based on duration of sales\
     orders as well as quotations',
    'website': 'http://www.aktivsoftware.com',
    'author': 'Aktiv Software',
    'license': 'AGPL-3',
    'description': 'Manages duration filtering for sale orders\
     and quotations.',
    'depends': ['base', 'sale_management'],
    'data': [
        'views/sale_order_filter_views.xml',
    ],
    'images': [],
    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'installable': True,
    'application': False,
}
