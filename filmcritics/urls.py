"""filmcritics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# my_project/urls.py
from django.contrib import admin
from django.urls import path, include,re_path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from film import views
from filmcritics import views
from django.conf.urls import url

urlpatterns = [
    path('film/', include('film.urls')),
    path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('accounts/', include('accounts.urls')),
    url(r'^accounts/', include(('accounts.urls','accounts'),namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^$', views.login_redirect, name = 'login_redirect'),
    #re_path(r'^like/$', views.like_post, name='like_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)