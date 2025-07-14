{
    'name': 'Library Management',
    'version': '1.0',
    'depends': ['base'],
    'category': 'Library',
    'author': 'Your Name',
    'description': 'Manage library books, authors and borrowing records.',
    'data': [
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_views.xml',
        'views/author_views.xml',
        'views/borrowing_views.xml',
    ],
    'installable': True,
    'application': True,
}
