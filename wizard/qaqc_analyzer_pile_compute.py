# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from calendar import monthrange
_logger = logging.getLogger(__name__)

class QaqcAnalyzerPileCompute(models.TransientModel):
    _name = 'qaqc.analyzer.pile.compute'

    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date(string="End Date", required=True)
    
    @api.multi
    def action_compute(self):    
        assay_piles = self.env['qaqc.assay.pile'].search([ ( 'active', '=', True ), ( 'date', '>=', self.start_date ), ( 'date', '<=', self.end_date ) ])
        assay_piles.action_reload()