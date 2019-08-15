import requests
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from . import services 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    category = services.main()

    