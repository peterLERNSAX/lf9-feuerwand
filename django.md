# Documentation for Django

## Content
- [Views](#views)

### Views

#### Index

```python
  class IndexView(View):
    """
    Index
    """ 

    def get(self,request:HttpRequest)->HttpResponse:
        """
        gets
        """
        return render(request,"ticketwand/index.html")
```

##### Methods

- `get` 

##### Templates

- `index.html`

##### Tests

- no

####

```python
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
``` 

##### Methods

- `get`
  - redners template with `CreateTicketForm`   
- `post` 
  - checks if `CreateTicketForm` is valid
  - redirects if form is invalid
  - creates `Ticket` if form is valid

##### Templates

- `ticket_created.html`
- `create_ticket.html`

##### Tests

- no
