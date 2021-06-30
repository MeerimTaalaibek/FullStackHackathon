"""MyCinematica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers, permissions
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from movies.views import MovieListView

schema_view = get_schema_view(
    info=openapi.Info(
        title='MyCinematica',
        default_version='V1',
        description='This is MyCinematica. Enjoy!!!',
        terms_of_service='http://www.google.com/policies/terms/',
        contact=openapi.Contact(email='test@gmail.com'),
        license=openapi.License(name='SUPER License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

router = routers.SimpleRouter()
# router.register('movies', MovieListView)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/profile/', include('movies.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include(router.urls)),
]





urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
urlpatterns += static(
     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)