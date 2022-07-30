"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
# config swegger ui
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# import api_urls
from rest_framework import permissions

from user_management.views import CustomAuthToken

# from user_management.views import Us

schema_view = get_schema_view(
   openapi.Info(
      title="FTB API Document",
      default_version='v1',
      description="FTB BANK SYSTEM",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="khaing.pho1991@gmail.com"),
      license=openapi.License(name="FTB License"),
   ),
   public=True,
   permission_classes=[permissions.IsAdminUser],
)

# JWT Config
from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
   TokenVerifyView
)

# router = DefaultRouter()
# router.register('', api_urls)

urlpatterns = [
   path('admin/', admin.site.urls),
   
   # swegger route
   # path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
   # API Route
   # /rest-auth/login
   # path('rest-auth/', include('rest_auth.urls')),
   # path('rest-auth/registration/', include('rest_auth.registration.urls')),
   
   # rest_framework route
   path('api/auth/', include('rest_framework.urls')),
   path('api/auth/login/', CustomAuthToken.as_view(), name="login"),
   
   # django_rest_auth
   # path('api/rest-auth/', include('rest_auth.urls')),
   # django-allauth
   # path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
   
   # allauth route
   # auth/account_login, account_logout, account_set_password
   # path('api/auth/', include('allauth.urls')),
   # auth/ signup/ [name='account_signup']
   # auth/ login/ [name='account_login']
   # auth/ logout/ [name='account_logout']
   # auth/ password/change/ [name='account_change_password']
   # auth/ password/set/ [name='account_set_password']
   # auth/ inactive/ [name='account_inactive']
   # auth/ email/ [name='account_email']
   # auth/ confirm-email/ [name='account_email_verification_sent']
   # auth/ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
   # auth/ password/reset/ [name='account_reset_password']
   # auth/ password/reset/done/ [name='account_reset_password_done']
   # auth/ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
   # auth/ password/reset/key/done/ [name='account_reset_password_from_key_done']
   
   # jwt route
   path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   
   # auth route
   # path('api/auth/login/', CustomAuthToken.as_view(), name="login"),
   
   path('api/users/', include('user_management.urls')),
   path('api/appraisal/', include('appraisal.urls'))
]
