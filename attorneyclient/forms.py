from django import forms
from .models import Client, Case
from crispy_forms.helper import FormHelper
 
class ClientForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
 
    class Meta:
        model = Client

class CaseForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
 
    class Meta:
        model = Case