# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    create_packs_according_packaging = fields.Boolean(string='Create packs according to packaging', default=False,
        help="If this case is checked,the system will create packs according to the selected packaging in the movement")

