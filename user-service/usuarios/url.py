# pyrefly: ignore [missing-import]
from django.urls import path
# pyrefly: ignore [missing-import]
from rest_framework.routers import DefaultRouter

from .views import UsuarioViewSet, LoginView


router = DefaultRouter()

router.register(
    r'usuarios',
    UsuarioViewSet,
    basename='usuario'
)

urlpatterns = router.urls
