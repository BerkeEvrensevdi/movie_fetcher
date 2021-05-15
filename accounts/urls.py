# accounts/urls.py
from django.urls import path

from . import views
from django.conf.urls import url

from django.urls import path,re_path,include
from . import views
from django.contrib.auth.views import login,logout
urlpatterns = [
    re_path(r'^$',views.home),
    url(r'^login/$',login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$',logout, {'template_name': 'accounts/logout.html'}),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^profile/$', views.view_profile, name='view_profile'),
    re_path(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    re_path(r'^change-password/$', views.change_password, name='change_password'),
    ]

"""
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
"""