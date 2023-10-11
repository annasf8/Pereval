from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from pick.views import PerevalViewSet

router = routers.DefaultRouter()
router.register(r'pereval', PerevalViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/submitData/', include(router.urls)),
    ]