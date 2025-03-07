from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
import itertools

from kassa.models import (
    IncomeKassaObject,
    ExpenseKassaObject
)
from products.models import (
    CommonProduct,
)
from export_import_products.models import (
    ImportProduct,
    ExportProduct,
    StoreProduct,
    ImShoppingCartObject,
    ExShoppingCartObject
)
from .models import (
    ReportingProduct
)
from .serializer import (
    ReportingProductSerializer
)
from django.forms.models import model_to_dict

######################################################################################
# --------------- CASH REPORT  -------------------------------------------------------------
######################################################################################

# --------------- Get Cash Report ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def get_cash_report(request):
    user = request.user

    if request.method == "POST":
        data = {}
        start_date = request.data["start_date"]
        end_date = request.data["end_date"]
        total_balance, total_income, total_expense, total_start_balance = calculateReport(start_date=start_date, end_date=end_date, account=user)
        data["total_balance"] = total_balance + total_start_balance
        data["total_income"] = total_income
        data["total_expense"] = total_expense
        data["total_start_balance"] = total_start_balance

        return Response(data=data)


def calculateReport(start_date, end_date, account):
    total_income = 0
    total_expense = 0
    total_balance = 0
    total_start_balance = 0
    incomes = IncomeKassaObject.objects.filter(date__range=[start_date, end_date], account=account)
    expenses = ExpenseKassaObject.objects.filter(date__range=[start_date, end_date], account=account)

    for income in incomes:
        total_income += int(income.fact_cash)
    
    for expense in expenses:
        total_expense += int(expense.fact_cash)

    total_balance = total_income - total_expense

    last_date_object = datetime.strptime(start_date, '%Y-%m-%d')
    last_date = (last_date_object - timedelta(days=1)).date()
    # print("/// date: "+str(last_date))
    # last_date_new_format = last_date.date()

    start_incomes = IncomeKassaObject.objects.filter(date__range=["2000-01-01", str(last_date)], account=account)
    start_expences = ExpenseKassaObject.objects.filter(date__range=["2000-01-01", str(last_date)], account=account)

    for start_income in start_incomes:
        total_start_balance += int(start_income.fact_cash)
    
    for start_expense in start_expences:
        total_start_balance -= int(start_expense.fact_cash)


    return total_balance, total_income, total_expense, total_start_balance


######################################################################################
# --------------- PRODUCT REPORT  -------------------------------------------------------------
######################################################################################

# --------------- Get Product Report ---------------
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def get_product_report(request):
    user = request.user
    if request.method == "POST":
        start_date = request.data["start_date"]
        end_date = request.data["end_date"]

        # product_list = [] 
        # sorted_prod_list = [] 
        # calculated_end_count_list = [] 
        # product_list_on_start = []
        # sorted_by_id_start_list = []
        # sorted_by_id_start_list = []
        # calculated_start_count_list = []

        # list between selected date:
        product_list = filterProductsReport(start_date, end_date, user)
        sorted_prod_list = sort_reporting_prods_by_id(product_list)
        calculated_end_count_list = calculate_reporting_prods_end_count(sorted_prod_list)


        # list until selected stert date:
        product_list_on_start = filterProductForStartCount(start_date=start_date, account=user)
        sorted_by_id_start_list = sort_reporting_prods_by_id(product_list_on_start)
        calculate_start_count_for_until_list = calculate_reporting_prods_starting_count(sorted_by_id_start_list)

        # calculate final list
        calculated_start_count_list = calculate_start_count_for_prods(list_before_start_date=calculate_start_count_for_until_list,
                                                                      list_after_start_date=calculated_end_count_list)
        

        # testing_list = test_list(list_before_start_date=calculate_start_count_for_until_list,
                                #  list_after_start_date=calculated_end_count_list)

        if len(product_list_on_start) != 0:
            # print("/// works \'if'\ part ") 

            ser = ReportingProductSerializer(calculated_start_count_list, many=True)
        else:
            # print("/// works \'else'\ part ") 
            ser = ReportingProductSerializer(calculated_end_count_list, many=True)

        # print("list objcs: ", len(product_list), " ", len(sorted_prod_list))
        # ser = ReportingProductSerializer(product_list_on_start, many=True)


        return Response(ser.data)
        # product_list = []



def filterProductsReport(start_date, end_date, account):
    prod_list = []
    
    import_products = ImportProduct.objects.filter(date__range=[start_date, end_date], account=account)
    export_products = ExportProduct.objects.filter(date__range=[start_date, end_date], account=account)

    for import_prod in import_products:
        store_product = import_prod.import_product
        company_product = store_product.company_product
        import_count = import_prod.prod_amount_in_cart

        reporting_prod = ReportingProduct(prod_id=store_product.product_id,
                                          prod_name=company_product.product_name,
                                          count_on_start="0",
                                          count_on_end="0",
                                          import_count=str(import_count),
                                          export_count="0"
        )

        prod_list.append(reporting_prod)

    for export_prod in export_products:
        store_product = export_prod.export_product
        company_product = store_product.company_product
        export_count = export_prod.prod_amount_in_cart

        reporting_prod = ReportingProduct(prod_id=store_product.product_id,
                                          prod_name=company_product.product_name,
                                          count_on_start="0",
                                          count_on_end="0",
                                          import_count="0",
                                          export_count=str(export_count)
        )

        prod_list.append(reporting_prod)

    return prod_list
    

def sort_reporting_prods_by_id(list):
    final_prod_list = []

    for prod in list:
        prod_id = prod.prod_id

        if len(final_prod_list) == 0:
            final_prod_list.append(prod)
        else:
            temporary_list = []
            tag = "not exist"

            for item in final_prod_list:
                if item.prod_id == prod_id:
                    tag = "exist"
                    item.import_count = int(item.import_count) + int(prod.import_count)
                    item.export_count = int(item.export_count) + int(prod.export_count)

            if tag == "not exist":
                final_prod_list.append(prod)

    return final_prod_list

        
def calculate_reporting_prods_end_count(list):
    for prod in list:
        end_count = int(prod.import_count) - int(prod.export_count)
        prod.count_on_end = end_count
    return list

def calculate_reporting_prods_starting_count(list):
    for prod in list:
        start_count = int(prod.import_count) - int(prod.export_count)
        prod.count_on_start = start_count
    return list

def filterProductForStartCount(start_date, account):
    prod_list = []
    last_date_object = datetime.strptime(start_date, '%Y-%m-%d')
    last_date = (last_date_object - timedelta(days=1)).date()

    import_products = ImportProduct.objects.filter(date__range=["2000-01-01", str(last_date)], account=account)
    export_products = ExportProduct.objects.filter(date__range=["2000-01-01", str(last_date)], account=account)

    for import_prod in import_products:
        store_product = import_prod.import_product
        company_product = store_product.company_product
        import_count = import_prod.prod_amount_in_cart

        reporting_prod = ReportingProduct(prod_id=store_product.product_id,
                                          prod_name=company_product.product_name,
                                          count_on_start="0",
                                          count_on_end="0",
                                          import_count=str(import_count),
                                          export_count="0"
        )

        prod_list.append(reporting_prod)

    for export_prod in export_products:
        store_product = export_prod.export_product
        company_product = store_product.company_product
        export_count = export_prod.prod_amount_in_cart

        reporting_prod = ReportingProduct(prod_id=store_product.product_id,
                                          prod_name=company_product.product_name,
                                          count_on_start="0",
                                          count_on_end="0",
                                          import_count="0",
                                          export_count=str(export_count)
        )

        prod_list.append(reporting_prod)

    return prod_list

def get_ids_from_list(list):
    ids = []
    for prod in list:
        ids.append(prod.prod_id)
    return ids

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def test_list(list_before_start_date, list_after_start_date):
    return list_before_start_date

def calculate_start_count_for_prods(list_before_start_date, list_after_start_date):

    final_sorted_list = []    
    until_list = list_before_start_date

    id_list = get_ids_from_list(list_after_start_date)
    until_list_ids = get_ids_from_list(until_list)

    ########## case when list_before_start_date < list_after_start_date
    if len(list_before_start_date) < len(list_after_start_date):
        for prod in list_after_start_date:
            final_sorted_list.append(prod)
        
        for prod in final_sorted_list:
            for until_prod in list_before_start_date:
                if until_prod.prod_id == prod.prod_id:
                    prod.count_on_start = until_prod.count_on_start
                    prod.count_on_end = int(prod.count_on_start) + int(prod.import_count) - int(prod.export_count)
                
    ########### case when list_after_start_date > list_after_start_date
    if len(list_before_start_date) >= len(list_after_start_date):
        for id in id_list:
            for prod in list_before_start_date:
                if prod.prod_id == id:
                    final_sorted_list.append(prod)

        for prod in final_sorted_list:
            for after_prod in list_after_start_date:
                if prod.prod_id == after_prod.prod_id:
                    prod.count_on_end = after_prod.count_on_end
                    prod.import_count = after_prod.import_count
                    prod.export_count = after_prod.export_count

        for prod in final_sorted_list:
            prod.count_on_end = int(prod.count_on_start) + int(prod.import_count) - int(prod.export_count)

    return final_sorted_list


