
from odoo.tools.translate import _
from odoo import http  
from odoo.http import request

class ProductController(http.Controller):
    """ The summary line for a class docstring should fit on one line.

        Routes:
          /some_url: url description
    """

    @http.route(['/shop/get_product_data'], type='json', auth="public", website=True)
    def get_desc(self, product_id,**kw):
        product_obj = request.env['product.template']
        product = product_obj.browse(product_id)
        print product.product_variant_ids[0]
        return {
            'id':product.id,
            'variant_id':product.product_variant_ids[0].id,
            'name':product.name,
            'image':product.image,
            'description_sale':product.description_sale,
            'number_of_variant':product.product_variant_count
            }
