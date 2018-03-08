"""tryten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import RestaurantDetailView,RestaurantCreateView,RestaurantListView

urlpatterns = [
    url(r'^$',RestaurantListView.as_view(),name="detail"),
    #url(r'^restaurant/create/$',restaurant_createview),
    url(r'^create/',RestaurantCreateView.as_view(),name="create"),
    url(r'^(?P<pk>\w+)/',RestaurantDetailView.as_view(),name="restaurants-detail"),
    #url(r'^(?P<pk>\w+)/edit/',RestaurantUpdateView.as_view(),name="edit"),


    #url(r'^restaurant/mexican/$',MexicanRestaurantListView.as_view()),
]
