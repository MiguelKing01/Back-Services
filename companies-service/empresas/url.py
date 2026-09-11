from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet


router = DefaultRouter()

router.register(
    r'empresas',
    CompanyViewSet,
    basename='empresa'
)

urlpatterns = router.urls