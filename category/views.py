#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from category.models import Category

# Create your views here.
def category_list(request):
	category_name = Category.objects.get()
	context = {
		'category_name': category_name,
	}

	return render_to_response('main.html',context)
