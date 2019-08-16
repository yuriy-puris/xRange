from rest_framework import viewsets

from .models import Category

from .serializers import CategorySerializer

from .services import CategoryParser

url = 'https://www.moyo.ua'

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  category = CategoryParser().get_category(url)
