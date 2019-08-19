from rest_framework import viewsets
from .models import Shops
from .serializers import ShopsSerializer

class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer