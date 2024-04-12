from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from quickstart.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]
