"""
urls
"""
from django.urls import path

from . import views

urlpatterns =[
    path("",views.IndexView.as_view(),name="index-view"),
    path("login/",views.LoginView.as_view(),name="login-view"),

]