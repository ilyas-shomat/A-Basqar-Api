from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta

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
        data["total_balance"] = total_balance
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

        product_list = filterProductsReport(start_date, end_date, user)
        ser = ReportingProductSerializer(product_list, many=True)

        return Response(ser.data)

def filterProductsReport(start_date, end_date, account):
    prod_list = []

    import_products = ImportProduct.objects.filter(date__range=[start_date, end_date], account=account)

    export_products = ExportProduct.objects.filter(date__range=[start_date, end_date], account=account)

    for import_prod in import_products:

        store_product = import_prod.import_product
        company_product = store_product.company_product
        import_count = import_prod.prod_amount_in_cart

        reporting_prod = ReportingProduct(prod_id=import_prod.im_prod_id,
                                          prod_name=company_product.product_name,
                                          count_on_start="0",
                                          count_on_end="0",
                                          import_count=str(import_count),
                                          export_count="0"
        )

        # reporting_prod = ReportingProduct()
        # reporting_prod.prod_id = import_prod.im_prod_id
        # store_product = import_prod.import_product
        # company_product = store_product.company_product
        # reporting_prod.prod_name = company_product.product_name
        prod_list.append(reporting_prod)

    return prod_list