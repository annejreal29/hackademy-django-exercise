"""hackademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from activity1.views import(
    profile_view,
    register,
    login_user,
    logout_user,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', profile_view, name='profile_view'),
    path('register/', register),
    path('login/', include("django.contrib.auth.urls")),
    path('login/', login_user),
    path('', logout_user, name='logout_user'),
    path('api/', include('api.urls')),  
    path('auth/', include('rest_authtoken.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)