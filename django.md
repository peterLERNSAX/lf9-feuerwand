# Documentation for Django

## Content
- [Views](#views)
- [Models](#models)
- [Forms](#forms)

---
---

## Views

### Index

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

#### Methods

- `get` 
  -  - redners template

#### Templates

- `index.html`

#### Tests

- no

---

### LoginView

```python
class LoginView(LoginView):
    """Login"""

    template_name = "ticketwand/login.html"
    success_url = "{% url 'index-view'%}"
```

#### Special

- `LoginView` from Django

#### Templates

- `login.html`

---

### CreateTicketView

```python
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

#### Methods

- `get`
  - redners template with `CreateTicketForm`   
- `post` 
  - checks if `CreateTicketForm` is valid
  - redirects if form is invalid
  - creates `Ticket` if form is valid

#### Templates

- `ticket_created.html`
- `create_ticket.html`

#### Tests

- no

---
---

## Models

### Ticket

```python
class Ticket(models.Model):
    """Model for Ticket"""

    status_choice = (
    ("in Bearbeitung", "in Bearbeitung"),
    ("nicht lösbar", "nicht lösbar"),
    ("reserveiert", "reserviert"),
)

    name = models.CharField(max_length=250,null=False,default="")
    text = models.TextField(null=False,default="")
    since = models.DateTimeField(null=False)
    creator_email = models.EmailField(null=False)
    status = models.CharField(null=True,choices=status_choice,max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(null=False,default=True)
    labels = models.TextField(null=True)
```

#### Fields

- `name` -> ticket headline
- `text` -> ticket text
- `since` -> creation date of the ticket
- `creator_email` -> email of the user who created the ticket
- `status` -> status of the ticket, see `status_choice`
- `owner` -> FK to django user model
- `is_active`-> bool if ticket is active
- `labels` -> textfield to be filled with labels

#### Tests

- no

---
---

## Forms

### CreateTicketForm

```python
class CreateTicketForm(forms.Form):
    """Create Ticket form"""

    name = forms.CharField(max_length=250,required=True)
    text = forms.Field(required=True)
    email = forms.EmailField(required=True)
```

### Fields

- `name` -> ticket headline
- `text` -> ticket text
- `email` -> email of the user who created the ticket

#### Tests

- no

---
---

