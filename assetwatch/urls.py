"""assetwatch URL Configuration

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
from django.urls import path, include,re_path
from dj_rest_auth.registration.views import VerifyEmailView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi





schema_view = get_schema_view(
    openapi.Info(
        title= 'AssetWatch API',
        default_version = 'version 1',
        description = '',
        contact= openapi.Contact(email='philipokiokio@gmail.com'),
        
        public = True,
        # permission_classes = (permissions.AllowAny,),
    )
)





urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),

    path('auth/password-reset/', include('django_rest_passwordreset.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('', include('asset.urls'))
    # path('api/', include('user.urls'))
    path('auth/account-confirm-email/',VerifyEmailView.as_view(),name='account_email_verification_sent'),
]
