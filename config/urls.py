from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from filmes.views import FilmeViewSet, FilmeAssistidoViewSet

router = DefaultRouter()
router.register(r'Filmes', FilmeViewSet)
router.register(r'FilmesAssistidos', FilmeAssistidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),     
]