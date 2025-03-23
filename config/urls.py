from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from filmes.views import FilmeViewSet

router = DefaultRouter()
router.register(r'Filmes', FilmeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),     
]