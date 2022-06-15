# -*- utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):

    _name = "library.book"
    _description = "Book Info"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")

    category = fields.Selection(
        string="Category",
        selection=[
            ("history", "History"),
            ("maths", "Maths"),
            ("language", "Language"),
        ],
        copy=False,
    )

    available = fields.Boolean(string="Available", default=True)
