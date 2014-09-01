from django.shortcuts import render_to_response
from website.models import Navigation

# Create your views here.
def nav_list(request):

	return render_to_response('newscenter.html',)

def nav(request):
	return render_to_response('homepage.html',)