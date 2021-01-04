from django.db import models

# Create your models here.
class ReportingProduct:
    
    def __init__(self, prod_id, prod_name, count_on_start, count_on_end, income, expense):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.count_on_start = count_on_start
        self.count_on_end = count_on_end
        self.income = income
        self.expense = expense

    # prod_id = 0
    # prod_name = ""
    # count_on_start = ""
    # count_on_end = ""
    # income = ""
    # expense = ""