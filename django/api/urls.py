from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import BrandViewSet, TemplateViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'brand', BrandViewSet)
router.register(r'template', TemplateViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url('api-auth/', include('rest_framework.urls')),
    url('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
