<<<<<<< HEAD
import requests
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from . import services 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    category = services.main()

    
=======
from rest_framework import viewsets

from .models import Category

from .serializers import CategorySerializer

from .services import CategoryParser

url = 'https://elmir.ua/'

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  category = CategoryParser().get_category(url)
>>>>>>> 61f010a93dd47c6b72c5c3748c4fb0b1459523fb
