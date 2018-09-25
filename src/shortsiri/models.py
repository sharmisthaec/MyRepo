# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from .validators import *

# Create your models here.

import random
import string
def shorter(size=8,chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for letter in range(8))

def create_code(instance,size=8):
	new_code=shorter(size=size)
	print(instance)
	print(instance.__class__)
	print(instance.__class__.__name__)
	Klass=instance.__class__
	qs_exist=Klass.objects.filter(shorturl=new_code).exists()
	if qs_exists:
		return create_code(size=size)
	return new_code
	



class sirimanager(models.Manager):
	def all(self,*args,**kwargs):
		qs_main=super(sirimanager,self).all(*args,**kwargs)
		qs=qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self,items=None):

		qs=siriurl.objects.filter(id__gte=1)
		if items is not None and isinstance(items,int):
			qs=qs.order_by('-id')[:items]
		new_codes=0
		for q in qs:
			q.shorturl=shorter(q)
			print(q.id)
			q.save()
			new_codes=new_codes+1
		return 'New codes made: {i}'.format(i=new_codes)




class siriurl(models.Model):
	address= models.CharField(max_length=200,validators=[validate_url,validate_dot_com])
	shorturl=models.CharField(max_length=15,unique=True)
	date=models.DateTimeField(auto_now=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	active=models.BooleanField(default=True)
	objects=sirimanager()

	def save(self,*args,**kwargs):
		if self.shorturl is None or self.shorturl=="":

			self.shorturl=shorter(self)
		print('It is saved')
		super(siriurl,self).save(*args,**kwargs)


	def __str__(self):
		return str(self.address)
	def __unicode__(self):
		return str(self.address)
