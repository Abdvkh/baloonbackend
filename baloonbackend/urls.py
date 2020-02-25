# from django.conf.urls import url
from core.views import TyresView, TyreViewSet

from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
# from core.views import search_by_size
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tyres', TyreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('api-auth/', include('rest_framework.urls')),
    path('', TyresView.as_view(), name='test'),
    # url(r"^(?P<width>\d+)/(?P<height>\d+)/(?P<radius>\d+\.\d+)$", SearchViewSet.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)