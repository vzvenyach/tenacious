from django.shortcuts import render
from .forms import ClientForm, CaseForm
from django.template import RequestContext

# Create your views here.

def add_client(request):
	context = RequestContext(request)
	return render(request, 'client.html', {'form': ClientForm()}, context_instance=RequestContext(request))

def add_case(request):
	context = RequestContext(request)
	return render(request, 'case.html', {'form': CaseForm(), 'form2':ClientForm()}, context_instance=RequestContext(request))