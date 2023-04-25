"""
views
"""
from django.shortcuts import render
from django.views import View
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.views import LoginView

# Create your views here.

class IndexView(View):
    """
    Index
    """ 

    def get(self,request:HttpRequest)->HttpResponse:
        """
        gets
        """
        return render(request,"ticketwand/index.html")

class LoginView(LoginView):
    """Login"""

    template_name = "ticketwand/login.html"
    success_url = "{% url 'index-view'%}"
