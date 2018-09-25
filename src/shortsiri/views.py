# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .models import siriurl
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from .forms import *



class HomeView(View):
	def get(self,request,*args,**kwargs):
		the_form=SubmitUrlForm()
		context={'title': 'Siri.com','form': the_form}
		return render(request, "home.html",context)


	def post(self,request,*args,**kwargs):
		form=SubmitUrlForm(request.POST)
		context={'title': 'Siri.com','form': form}
		page="home.html"
		if form.is_valid():
			new_url=form.cleaned_data.get('url')
			obj,created=siriurl.objects.get_or_create(address=new_url)
			context={'object':obj,'created':created,}
			if created:
				page='success.html'
			else:
				page='exists.html'
		return render(request,page,context)


class siriview(View):
	def get(self, request,shorturl=None,*args,**kwargs):
		obj=get_object_or_404(siriurl,shorturl=shorturl)
		return HttpResponseRedirect(obj.address)

	def post(self,request,*args,**kwargs):
		return HttpResponse()
