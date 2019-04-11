from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import BrandViewSet, TemplateViewSet, MailViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'brand', BrandViewSet)
router.register(r'template', TemplateViewSet)
router.register(r'mail', MailViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url('api-auth/', include('rest_framework.urls')),
    url('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
