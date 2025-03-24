from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from filmes.views import FilterFilmeViewSet  

router = DefaultRouter()
router.register(r'FilterFilmes', FilterFilmeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),     
]