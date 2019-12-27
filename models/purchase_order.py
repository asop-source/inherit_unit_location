from odoo import models, fields, api
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)


from . import default



class PurchaseOrder(models.Model):
	_inherit = "purchase.order"


	
	def _get_default_unit(self):
		user = self.env.user
		return default.get_default_unit(self, user, _logger)

	def _get_default_location(self):

		user = self.env.user
		return default.get_default_location(self, user, _logger)


		

	unit_id = fields.Many2one(readonly=True, comodel_name='hr.department', string='Unit',default=_get_default_unit)
	analytic_tag_ids = fields.Many2one(readonly=True ,comodel_name='account.analytic.tag', string='Location',default=_get_default_location)

