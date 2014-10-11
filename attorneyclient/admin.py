from django.contrib import admin

# Register your models here.
from attorneyclient.models import Client, Record, Form

admin.site.register(Client)
admin.site.register(Record)
admin.site.register(Form)