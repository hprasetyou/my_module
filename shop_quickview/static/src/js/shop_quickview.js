odoo.define('shop_quickview', function (require) {
    "use strict";
    
    var ajax = require('web.ajax');
    var Model = require('web.Model');
    $(document).ready(function () {
        
        $('.btn_quickview').click(function(e){
            e.preventDefault()
            var id = $(this).parents('.oe_product_image').find('span[itemprop="image"]').data('oe-id')
            var link = $(this).parents('.oe_product_cart').find('h5 a').attr('href')
            
            ajax.jsonRpc("/shop/get_product_data", "call", {
                'product_id' : parseInt(id)
            }).then(function (data){
                console.log(data);
                var img = data.image
                var prodname = data.name
                $('#prodDetail').find('.img').attr('src','/web/image/product.template/'+id+'/image/300x300')
                $('#product_id').val(data.variant_id)
                $('#productTitle').text(prodname)
                $('#product-detail').attr('href',link)
                $('#prodDescription').text(data.description_sale)
                if(data.number_of_variant > 1){
                    $('#product-detail').show()
                    $('#add-cart-form').hide()
                }else{
                    $('#product-detail').hide()
                    $('#add-cart-form').show()
                }
                $('#prodDetail').modal('show')
            })
        })
        $('.oe_product_image').on('mouseover',function(e){
            $(this).find('.prod_layer').stop().slideDown('fast')
                       
        })
        $('.oe_product_image').on('mouseout',function(e){
            $(this).find('.prod_layer').stop().slideUp()  
        })
        
    })
})