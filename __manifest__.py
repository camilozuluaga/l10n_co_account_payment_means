# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name': 'l10n_co account payment means',
	'version': '1.0',
	'website': '',
	'category': 'Localizacion',
	'summary': 'l10n_co account payment means',
	'description': """
		modulo para el manejo de la informacion de las formas de pago de la factura

	""",
	'depends': [
		'account'
	],
	'data': [
		'data/account_payment_mean_code_data.xml',
		'views/account_payment_mean_code.xml',
		'security/ir.model.access.csv',
		
	],
	'installable': True,
	'auto_install': False,
	'application': True,
}
