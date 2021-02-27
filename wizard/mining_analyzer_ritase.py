# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from calendar import monthrange
_logger = logging.getLogger(__name__)

class MiningAnalyzerRitase(models.TransientModel):
    _name = 'mining.analyzer.ritase'

    @api.model
    def _default_config(self):
        ProductionConfig = self.env['production.config'].sudo()
        production_config = ProductionConfig.search([ ( "active", "=", True ) ]) 
        if not production_config :
            raise UserError(_('Please Set Configuration file') )
        return production_config[0]

    production_config_id = fields.Many2one('production.config', string='Production Config', default=_default_config )

    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date(string="End Date", required=True)

    @api.multi
    def action_analyze(self):    
        ritase_orders = self.env['production.ritase.order'].search([ ( 'date', '>=', self.start_date ), ( 'date', '<=', self.end_date ) ], order="date asc, shift asc")
        message = ""
        for ritase_order in ritase_orders:
            for counter in ritase_order.counter_ids:
                counter.repair()

            if ritase_order.product_id.id not in self.production_config_id.other_product_ids.ids:
                if ritase_order.product_uom_qty == 0:
                    message += "Ritase ["+ ritase_order.name +"] tonnase cannot be 0! \n"
                    # raise UserError(_('Ritase [%s] tonnase cannot be 0! ') %( ritase_order.name ) )
            for counter in ritase_order.counter_ids:
                if self.production_config_id.rit_vehicle_tag_id.id not in counter.vehicle_id.tag_ids.ids :
                    message += "Only Dump Truck allowed to fill ritase form ["+ritase_order.name+"]. \n"
                    # raise UserError(_('Only Dump Truck allowed to fill ritase form [%s]') %( ritase_order.name ) )
        
        # if message == "" :
        #     raise UserError(_('It Seems Okay') )
        # else :
        #     raise UserError(_( message ) )

        return True    
        