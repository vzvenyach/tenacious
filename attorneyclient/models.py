from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

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
