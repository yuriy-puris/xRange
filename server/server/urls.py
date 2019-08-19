from django.contrib import admin
from django.urls import path, include
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include(router.urls)),
    path('category/', include(router.urls)),
    path('shops/', include(router.urls))
]
