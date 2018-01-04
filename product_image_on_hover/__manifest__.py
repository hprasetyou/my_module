{
    'name': 'Product image on hover',
    'version': '1.0',
    'depends': ['web','product'],
    'author': 'Heru Prasetyo Utomo',
    'website': "http://hprasetyou.com",
    'description': """
        Show image of product when you hover on product
    """,
    'category': 'Inventory',
    'sequence': 1,
    'js': 'static/src/js/product_image_on_hover.js',
    'data': ['product_image_on_hover.xml'],
    'images': [
        'static/description/ss2.png',
        'static/description/ss1.png',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
