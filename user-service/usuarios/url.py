from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UsuarioViewSet, LoginView


router = DefaultRouter()

router.register(
    r'usuarios',
    UsuarioViewSet,
    basename='usuario'
)

urlpatterns = router.urls + [
    path('token/', LoginView.as_view(), name='token'),
]