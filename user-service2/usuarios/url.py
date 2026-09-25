<<<<<<< HEAD
=======
# pyrefly: ignore [missing-import]
from django.urls import path
# pyrefly: ignore [missing-import]
>>>>>>> f72d74c67228fa038055226b6b185960280e30f2
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet


router = DefaultRouter()

router.register(
    r'usuarios',
    UsuarioViewSet,
    basename='usuario'
)

<<<<<<< HEAD
urlpatterns = router.urls
=======
urlpatterns = router.urls
>>>>>>> f72d74c67228fa038055226b6b185960280e30f2
