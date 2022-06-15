# -*- coding: utf-8 =*-

{
    "name": "Library Management",
    "summary": """Management app to manage library""",
    "description": """
        Management Module to manage library:
        - Books
        - Librarian
        - Customer
    """,
    "author": "Andrew",
    "website": "https://www.odoo.com",
    "category": "Management",
    "version": "0.1",
    "depends": ["base"],
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/library_menuitems.xml",
        "views/book_views.xml",
    ],
    "demo": [
        "demo/library_demo.xml",
    ],
}
