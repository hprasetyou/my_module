# -*- coding: utf-8 -*-
{
    'name': "Filter Picking Ready",
    'depends': ['stock'],
    'author': "Hasan Mahfud",
    'website': "hprasetyou.com",
    'category': "Stock",
    'summary': "Filter Picking That Only Have Picking Ready",
    'description': """
    - Filter Picking That Only Have Picking Ready
    - odoo version 10
    """,
    'data':[
        "views/stock_picking_views.xml"],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
    'application': False,
    'auto-install': False,
}
