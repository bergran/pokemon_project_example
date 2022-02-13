"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', include('pokemon.urls')),
    path('', include('team.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('dj_rest_auth.urls')),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

if settings.DEBUG:
    from rest_framework.schemas import get_schema_view

    urlpatterns.append(
        path('api/docs/schema', get_schema_view(
            title="Your Project",
            description="API for all things …",
            permission_classes=[AllowAny],
            version='0.0.1'
        ), name='openapi-schema'),
    )
    urlpatterns.append(
        path('api/docs', TemplateView.as_view(
            template_name='docs/swagger-ui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ), name='swagger-ui'),
    )
