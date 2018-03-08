# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from datetime import datetime
from django.db import models
from django.conf import settings
from validators import validate_category
from django.core.urlresolvers import reverse
#Create your models here.

User=settings.AUTH_USER_MODEL
class Restaurant(models.Model):
	owner=models.ForeignKey(User)
	name=models.CharField(max_length=150)
	#dob = models.DateField(null=True)
	location=models.CharField(max_length=100,blank=True,null=True)
	category=models.CharField(max_length=120,null=True,blank=True,validators=[validate_category])
	timestamp=models.DateTimeField(auto_now_add=True)
	#date=models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:restaurants-detail',kwargs={'pk':self.pk })