from odoo import api, models, fields


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    previous_move_id = fields.Many2one(
        'account.move', string='Cancelled Accounting Entry Reference')

    # @api.multi
    # def action_payslip_cancel(self):
    #     flag = self.env['ir.model.fields'].search(
    #         [('model', '=', 'hr.payslip'), ('name', '=', 'move_id')])
    #     for slip in self:

    #         if slip.company_id.cancel_payslip:
    #             if flag and slip.move_id:
    #                 if slip.move_id.journal_id:
    #                     slip.move_id.journal_id.update_posted = True
    #                 slip.move_id.button_cancel()
    #                 slip.move_id.unlink()
    #             slip.write({'state': 'cancel'})

    #     return super(HrPayslip, self).action_payslip_cancel()

    @api.multi
    def action_payslip_cancel(self):
        flag = self.env['ir.model.fields'].search(
            [('model', '=', 'hr.payslip'), ('name', '=', 'move_id')])
        for slip in self:
            if slip.company_id.cancel_payslip:
                if flag and slip.move_id:
                    if slip.move_id.journal_id:
                        slip.move_id.journal_id.update_posted = True
                    slip.move_id.button_cancel()
                    # slip.move_id.unlink()
                    slip.previous_move_id = slip.move_id.id
                    slip.move_id = False
                slip.write({'state': 'cancel'})

        # return super(HrPayslip, self).action_payslip_cancel()
