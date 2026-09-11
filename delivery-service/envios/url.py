from rest_framework.routers import DefaultRouter
from .views import EnvioViewSet


router = DefaultRouter()

router.register(
    r'envios',
    EnvioViewSet,
    basename='envio'
)

urlpatterns = router.urls
