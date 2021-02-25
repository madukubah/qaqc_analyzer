# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from calendar import monthrange
_logger = logging.getLogger(__name__)

class MiningAnalyzerHourmeter(models.TransientModel):
    _name = 'mining.analyzer.hourmeter'

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
        Vehicle = self.env['fleet.vehicle'].sudo()
        vehicles = Vehicle.search( [ ( "tag_ids", "in", self.production_config_id.hm_vehicle_tag_id.id ) ] )
        message = ""
        for vehicle in vehicles:
            hourmeter_logs = self.env['production.vehicle.hourmeter.log'].search([ ( 'date', '>=', self.start_date ), ( 'date', '<=', self.end_date ), ( 'vehicle_id', '=', vehicle.id ) ], order="date asc, start_datetime asc")
            # for ind, hourmeter_log in enumerate( hourmeter_logs ):
            for ind in range( len( hourmeter_logs ) ):
                if hourmeter_logs[ ind ].value > 20 :
                    message += "["+vehicle.name+"] found anomaly at "+hourmeter_logs[ ind ].date+" \n"
                if ind == 0 : continue
                if round( hourmeter_logs[ ind-1 ].end, 2 ) != round( hourmeter_logs[ ind ].start, 2 ) :
                    message += "["+vehicle.name+"] Hourmeter didn`t match at "+hourmeter_logs[ ind-1 ].date+"("+str( hourmeter_logs[ ind-1 ].end )+") to "+hourmeter_logs[ ind ].date+"("+str( hourmeter_logs[ ind ].start )+") \n"

        if message == "" :
            raise UserError(_('It Seems Okay') )
        else :
            raise UserError(_( message ) )
        
        return True    
        