# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import fields
from odoo.tools.misc import Sentinel, SENTINEL

def __init__(self, selection=SENTINEL, string: str | Sentinel = SENTINEL, **kwargs):
    if kwargs.get("select_year", False):
        starting_year = kwargs.get("starting_year", 1900)
        ending_year = kwargs.get("ending_year", datetime.now().year)
        selection = [(str(year), str(year)) for year in range(starting_year, ending_year + 1)]

    super(fields.Selection, self).__init__(selection=selection, string=string, **kwargs)
    self._selection = dict(selection) if isinstance(selection, list) else None

setattr(fields.Selection, "__init__", __init__)