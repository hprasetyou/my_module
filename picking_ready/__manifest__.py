# -*- coding: utf-8 -*-
{
    'name': "Filter Picking Ready",
    'depends': ['stock'],
    'author': "Heru Prasetyo Utomo",
    'website': "http://hprasetyou.com",
    'category': "Stock",
    'summary': "Filter Picking That Only Have Picking Ready",
    'description': """
    - create filter Stock Picking Type That Only Have Picking Ready
    - odoo version 10
    """,
    'images': [
            'static/description/ss.png',
    ],
    'data':[
        "views/stock_picking_views.xml"],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
    'application': False,
    'auto-install': False,
}
