# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PaymentMethod(models.Model):
    _inherit = 'sale.order'

    method = fields.Selection([('cash', 'Cash'), ('credit', 'Credit')], string='Type', required=True, default='cash')


    def confirmation(self):
        for sale in self:

            if sale.type == 'cash':
                super().action_confirm()

            else:
                raise ValidationError("You are not allowed to confirm a credit sales order!")
        
