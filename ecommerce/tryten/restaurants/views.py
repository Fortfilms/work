# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404

import random
from django.db.models import Q
from models import Restaurant
from .forms import RestaurantCreateForm,RestaurantLocationCreateForm


class ContactView(TemplateView):
	template_name="contact.html"
	def get_context_data(self,*args,**kwargs):
		context=super(ContactView,self).get_context_data(*args,**kwargs)
		num=None
		random1=random.randint(0, 100000000),
		some_list={random.randint(0, 100000000),random.randint(0, 100000000),random.randint(0, 100000000)}
		condition_bool_item=True
		if condition_bool_item:
			num=random.randint(0, 100000000)
		context={
		"html_var":"context_veriable",
		"num": num,
		"some_list":some_list
		}
		print context
		return context


class AboutView(TemplateView):
	template_name="about.html"
	def get_context_data(self,*args,**kwargs):
		context=super(AboutView,self).get_context_data(*args,**kwargs)
		num=None
		random1=random.randint(0, 100000000),
		some_list={random.randint(0, 100000000),random.randint(0, 100000000),random.randint(0, 100000000)}
		condition_bool_item=True
		if condition_bool_item:
			num=random.randint(0, 100000000)
		context={
		"html_var":"context_veriable",
		"num": num,
		"some_list":some_list
		}

		print context
		return context


class HomeView(TemplateView):
	template_name="home.html"
	def get_context_data(self,*args,**kwargs):
		context=super(HomeView,self).get_context_data(*args,**kwargs)
		num=None
		random1=random.randint(0, 100000000),
		some_list={random.randint(0, 100000000),random.randint(0, 100000000),random.randint(0, 100000000)}
		condition_bool_item=True
		if condition_bool_item:
			num=random.randint(0, 100000000)
		context={
		"html_var":"context_veriable",
		"num": num,
		"some_list":some_list
		}

		print context
		return context


# def restaurant_listview(request):
# 	template_name="restaurants/restaurants_list.html"
# 	query=Restaurant.objects.all()
# 	context={
# 	"list":query,
# 	}
# 	return render(request,template_name,context)


class RestaurantListView(LoginRequiredMixin,ListView):
	def get_queryset(self):
		return  Restaurant.objects.filter(owner=self.request.user)


# @login_required(login_url="/login/")
# def restaurant_createview(request):
# 	form=RestaurantLocationCreateForm(request.POST)
# 	errors=None
# 	if form.is_valid():
# 		if request.user.is_authenticated():
# 			instance=form.save(commit=False)
# 			instance.owner=request.user
# 			instance.save()
# 			return HttpResponseRedirect("/restaurant/")
# 		else:
# 			return HttpResponseRedirect("/login/")
# 	if form.errors:
# 		errors=form.errors 
# 	#if request.method=="GET":
# 	#	print "get data"
# 	#if request.method=="POST":
# 	#	print "post data"
# 	#	print request.POST
# 	#	title=request.POST.get("title")
# 	#	location=request.POST.get("location")
# 	#	category=request.POST.get("category")
# 	#	obj=Restaurant.objects.create(
# 	#		name=title,
# 	#		location=location,
# 	#		)
		

# 	template_name="restaurants/form.html"
# 	context={"form":form,"errors":errors}
# 	return render(request,template_name,context)



# class RestaurantDetailView(LoginRequiredMixin,DetailView):
# 	def get_queryset(self):
# 		return  Restaurant.objects.filter(owner=self.request.user)
	

class RestaurantCreateView(LoginRequiredMixin,CreateView):
	form_class=RestaurantLocationCreateForm
	login_url="/login/"
	template_name='restaurants/form.html'
	success_url="/restaurant/"

	def form_valid(self,form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		return super(RestaurantCreateView,self).form_valid(form)



class RestaurantDetailView(LoginRequiredMixin,UpdateView):
	form_class=RestaurantLocationCreateForm
	template_name="restaurants/restaurant_detail.html"
	model=Restaurant
	login_url="/login/"
	success_url="/restaurant/"

	def get_queryset(self):
		return  Restaurant.objects.filter(owner=self.request.user)

	def form_valid(self,form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		return super(RestaurantDetailView,self).form_valid(form)

	def get_context_data(self,*args,**kwargs):
		context=super(RestaurantDetailView,self).get_context_data(*args,**kwargs)
		context['title']="Create Item"
		return context


# class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
#     form_class = RestaurantCreateForm
#     model = Restaurant
#     template_name = 'restaurants/restaurant_detail.html'

#     def get(self, request, **kwargs):
#         self.object = Restaurant.objects.get(id=self.request.id)
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         context = self.get_context_data(object=self.object, form=form)
#         return self.render_to_response(context)

#     def get_object(self, queryset=None):
#         obj = Restaurant.objects.get(id=self.request.id)
#         return obj




