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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    # re_path(r'auth/registration/verify/(?P<key>[-:\w]+)/$',VerifyEmailView.as_view()),

    path('auth/password-reset/', include('django_rest_passwordreset.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('', include('asset.urls'))
    # path('api/', include('user.urls'))
    path('auth/account-confirm-email/',VerifyEmailView.as_view(),name='account_email_verification_sent'),
]
