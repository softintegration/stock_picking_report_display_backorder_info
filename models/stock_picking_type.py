# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    enable_backorder_info_delivery_report = fields.Boolean(string='Display backorder informations in delivery report', default=True)

