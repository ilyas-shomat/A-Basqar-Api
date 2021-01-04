from django.db import models

# Create your models here.
class ReportingProduct:
    
    def __init__(self, prod_id, prod_name, count_on_start, count_on_end, import_count, export_count):
        self.prod_id = prod_id
        self.prod_name = prod_name
        self.count_on_start = count_on_start
        self.count_on_end = count_on_end
        self.import_count = import_count
        self.export_count = export_count

    # prod_id = 0
    # prod_name = ""
    # count_on_start = ""
    # count_on_end = ""
    # income = ""
    # expense = ""