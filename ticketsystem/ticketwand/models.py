"""
Models
"""

from django.db import models
from django.contrib.auth.models import User # new

# Create your models here.

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


