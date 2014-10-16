from django.shortcuts import render
from .forms import ClientForm
from django.template import RequestContext

# Create your views here.

def add_client(request):
	context = RequestContext(request)
	return render(request, 'client.html', {'form': ClientForm()}, context_instance=RequestContext(request))