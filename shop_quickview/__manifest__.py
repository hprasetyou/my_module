# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Heru Prasetyo Utomo
#    Copyright 2018 Heru Prasetyo Utomo
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# noinspection PyStatementEffect
{
    'name': 'Product Sales Quickview',
    'version': '1.0',
    'depends': ['website_sale'],
    'author': 'Heru Prasetyo Utomo',
    'website': "http://hprasetyou.com",
    'summary': "Show pop up to quickview and add product to cart",
    'description': """
        Show pop up to quickview and add product to cart
    """,
    'category': 'eCommerce',
    'sequence': 1,
    'data': ['views/templates.xml'],
    'images': [
        'static/description/2.png',
        'static/description/1.png',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
