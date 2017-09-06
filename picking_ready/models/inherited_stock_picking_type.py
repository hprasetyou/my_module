from odoo import _, fields, models, api

class InheritedStockPickingType(models.Model):

    _inherit = ['stock.picking.type']

    pickings = fields.One2many(
        string= 'Ready Picking',
        comodel_name='stock.picking',
        inverse_name='picking_type_id'
    )

    count_ready = fields.Integer(
        string=u'Count Ready',
        compute='_compute_ready',
        
    )
    
    @api.one
    def _compute_ready(self):
        search_ready = self.env.get('stock.picking').search_count([('state','=','assigned'),('picking_type_id','=',self.id)])
        print search_ready
        self.count_ready = 1
        