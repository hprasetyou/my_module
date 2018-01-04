# -*- coding: utf-8 -*-
{
    'name': "Filter Picking Ready",
    'depends': ['stock'],
    'author': "Heru Prasetyo Utomo",
    'website': "http://hprasetyou.com",
    'category': "Stock",
    'summary': "Filter Picking That Only Have Picking Ready",
    'description': """
    - Filter Stock Picking Type That Only Have Picking Ready
    - odoo version 10
    """,
    'price': 0.99,
    'currency':'USD',
    'data':[
        "views/stock_picking_views.xml"],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
    'application': False,
    'auto-install': False,
}
