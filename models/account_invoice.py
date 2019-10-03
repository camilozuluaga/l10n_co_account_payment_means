# -*- coding: utf-8 -*-
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
   
	_inherit = "account.invoice"

	# Establece por defecto el medio de pago Efectivo
	payment_means_code_id  = fields.Many2one(
		'account.payment.mean.code',
		string='Método de pago',
		copy=False,
		required=True,
		default=lambda self: self.env['account.payment.mean.code'].search([('code', '=', '10')], limit=1)
	)

