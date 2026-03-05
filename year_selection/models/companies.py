FOR USED

class COMPANIESINHERIT(models.Model):
    _inherit = 'res.companies'
    
    since = fields.Selection(string="Berdiri sejak", select_year=True, starting_year=1900, ending_year=2020)