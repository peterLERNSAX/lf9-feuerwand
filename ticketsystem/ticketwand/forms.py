"""forms"""
from django import forms

class CreateTicketForm(forms.Form):
    """Create Ticket form"""

    name = forms.CharField(max_length=250,required=True)
    text = forms.Field(required=True)
    email = forms.EmailField(required=True)
