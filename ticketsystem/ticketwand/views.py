"""
views
"""
from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.views import LoginView
from datetime import datetime


from .forms import CreateTicketForm
from .models import Ticket


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

class CreateTicketView(View):
    """Create Ticket"""

    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        form = CreateTicketForm()
        return render(request,"ticketwand/create_ticket.html",{"form":form})
    
    def post(self,request:HttpRequest)->HttpResponse:
        """post"""
        form = CreateTicketForm(data=request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            title = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            Ticket.objects.create(name=title,text=text,creator_email=email,since=datetime.now())
            return render(request,"ticketwand/ticket_created.html")
        return redirect("create-ticket-view")
    