from odoo import models, fields, api
from datetime import timedelta

class LibraryBorrow(models.Model):
    _name = 'library.borrow'
    _description = 'Borrowing Record'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    partner_id = fields.Many2one('res.partner', string='Borrower', required=True)
    borrow_date = fields.Date(default=fields.Date.today)
    return_date = fields.Date()
    returned = fields.Boolean('Returned', default=False)

    @api.onchange('borrow_date')
    def _onchange_borrow_date(self):
        if self.borrow_date:
            self.return_date = self.borrow_date + timedelta(days=7)

    def mark_as_returned(self):
        for record in self:
            record.returned = True
            record.book_id.is_available = True
