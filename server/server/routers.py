from rest_framework import routers
from products.viewsets import ProductViewSet
from category.viewsets import CategoryViewSet
from shops.viewsets import ShopsViewSet

router = routers.DefaultRouter()

router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'shops', ShopsViewSet)