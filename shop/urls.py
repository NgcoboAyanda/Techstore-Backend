from rest_framework.routers import DefaultRouter
from shop.views import GetAllProductsViewSet

router = DefaultRouter()
router.register(r'all', GetAllProductsViewSet, basename='all-products' )
urlpatterns = router.urls