from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char('Title', required=True)
    author_id = fields.Many2one('library.author', string='Author', required=True)
    description = fields.Text()
    publish_date = fields.Date()
    is_available = fields.Boolean('Available', default=True)
