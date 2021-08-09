"""app URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name= 'user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'user/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('create/', user_views.InfoCreateView.as_view(), name="create"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='api token'),
    path('check/', user_views.CheckView.as_view(), name='check'),
]
