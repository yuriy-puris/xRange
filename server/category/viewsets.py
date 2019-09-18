from rest_framework import viewsets

from .models import CategoryMoyo
from shops.models import Shops

from .serializers import CategorySerializer

from .services import CategoryParser



def get_shop():
    eldorado = Shops.objects.all()[1]
    category = CategoryParser().get_category(eldorado.shop_url)

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = CategoryMoyo.objects.all()
  serializer_class = CategorySerializer
  
  category = get_shop()