from django.shortcuts import render
from django.views import View
from django.http import HttpRequest,HttpResponse

# Create your views here.

class IndexView(View):
    """
    Index
    """ 

    def get(self,request:HttpRequest)->HttpResponse:
        """
        get
        """
        return render(request,"ticketwand/index.html") 