from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import (
    Common_Category,
    Each_Company_Category,
    Common_Product,
    Each_Company_Product,
    Each_Store_Product
)

from .serializer import (
    CommonCategorySerializer,
    EachCompanyCategorySerializer,
    CommonProductSerializer,
    EachCompanyProductSerializer,
    EachStoreProductProductSerializer,
)

######################################################################################
# --------------- COMMON -------------------------------------------------------------
######################################################################################

# --------------- Get All Common Categories ---------------
@api_view(["GET"])
def get_all_common_categories(request):
    common_categories = Common_Category.objects

    if request.method == "GET":
        ser = CommonCategorySerializer(common_categories, many=True)

    return Response(ser.data)

# --------------- Get Each Company Categories ---------------
# --------------- Get All Common Products ---------------
# --------------- Get Each Company Products ---------------
# --------------- Get Each Store Products ---------------



