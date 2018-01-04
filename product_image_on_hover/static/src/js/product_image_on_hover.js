odoo.define("product_image_on_hover.ListView", function (require) {
"use strict";

    var ListView = require("web.ListView");
    var KanbanView = require("web_kanban.KanbanView");
    var FormView = require("web.FormView");
    // var Model = require('web.DataModel');
    // var Product = new Model('product.template');
    ListView.include({
        // do something 
        do_show: function () {
            // var product = this.records.records
            if (this.dataset.model == 'product.template' || this.dataset.model == 'product.product'){
                this.$el.find('tbody').find('tr').popover(
                    {
                        'content': function(e){
                            return '<img src="/web/image?model=product.template&id='+ $(this).attr('data-id') +'&field=image_medium" class="img-responsive" />'
                        },
                        'html': true,
                        'placement':  function(c,s){
                            return $(s).position().top < 200 ?'bottom':'top'
                        },
                        'trigger': 'hover',
                    });
            }
            return this._super();
        }
    });
    KanbanView.include({
        do_show: function(){
            if (this.dataset.model == 'product.template' || this.dataset.model == 'product.product'){
                this.$el.find('.o_kanban_record').popover({
                        'content': function(e){
                            return '<img src="'+$(this).find('.o_kanban_image').children().attr('src')+'" />'
                        },
                        'title': function(){
                            return $(this).find('.oe_kanban_details').find('strong').html()
                        },
                        'html': true,
                        'placement': function(c,s){
                            return $(s).position().top < 200 ?'bottom':'top'
                        },
                        'trigger': 'hover',
                    })
            }
         return this._super();
        }
    })

    

});
