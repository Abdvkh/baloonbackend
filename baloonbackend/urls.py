from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import TyreViewSet, SearchViewSet
from django.conf.urls.static import static
from django.conf import settings
# from core.views import search_by_size

router = routers.DefaultRouter()
router.register(r'tyres', TyreViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r"^(?P<width>\d+)/(?P<height>\d+)/(?P<radius>\d+\.\d+)$", SearchViewSet.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
