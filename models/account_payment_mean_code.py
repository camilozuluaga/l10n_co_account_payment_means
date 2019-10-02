# -*- coding: utf-8 -*-
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)

class AccountPaymentMeanCode(models.Model):


	_name = 'account.payment.mean.code'


	name = fields.Char(string=u'Method')
	code = fields.Char(string=u'Code')

