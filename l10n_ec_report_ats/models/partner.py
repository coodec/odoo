# -*- coding: utf-8 -*-
from openerp import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'
    
    tipopago_id = fields.Many2one('l10n_ec_sri_ats_16.tipopago',
                                      string='Tipo de pago principal', help="Se usa en caso de que el ATS sea generado antes de que se realice el pago")
    formapago_id = fields.Many2one('l10n_ec_sri_ats_16.formapago',
                                      string='Forma de pago principal', help="Se usa en caso de que el ATS sea generado antes de que se realice el pago")
            
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
