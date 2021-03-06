from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True) 
    phone_number = models.CharField(max_length=30, blank=True, null=True)

class Case(models.Model):
    case_number = models.CharField(max_length=30)
    status = models.CharField(max_length=6, choices=(('Open','Open'),('Closed','Closed')), default='Open')
#    landlord = models.CharField(max_length=50)
 #   tenant = models.CharField(max_length=50)

class Form(models.Model):
    form_name = models.CharField(max_length=200)

class FormField(models.Model):
    form = models.ForeignKey(Form)

class Record(models.Model):
    attorneys = models.ManyToManyField(User)
    client = models.ManyToManyField(Client)
    form = models.ForeignKey(Form)

class RecordField(models.Model):
    record = models.ForeignKey(Record)
