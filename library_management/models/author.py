from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char('Name', required=True)
    book_ids = fields.One2many('library.book', 'author_id', string='Books')
