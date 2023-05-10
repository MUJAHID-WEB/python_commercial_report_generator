
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
# from django.conf import settings
# from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from report_api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r"Reports", views.ReportView)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path("", include('report_api.urls', namespace='report_api')),
    path("api/", include(router.urls)),
    # API schema and Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name = "schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name = "schema")),
]
