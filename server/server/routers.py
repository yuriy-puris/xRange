from rest_framework import routers
from products.viewsets import ProductViewSet
from category.viewsets import CategoryViewSet

router = routers.DefaultRouter()

router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)