# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
from core.views import TestView
from django.conf.urls.static import static
from django.conf import settings
# from core.views import search_by_size
from rest_framework.authtoken.views import obtain_auth_token
# router = routers.DefaultRouter()
# router.register(r'tyres', TestView)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', TestView.as_view(), name='test'),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='obtain-token')
    # url(r"^(?P<width>\d+)/(?P<height>\d+)/(?P<radius>\d+\.\d+)$", SearchViewSet.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)