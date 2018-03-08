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
from .views import (
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
    ItemCreateView,
    )
urlpatterns = [
    url(r'^$',ItemListView.as_view(),name="list"),
    #url(r'^restaurant/create/$',restaurant_createview),
    url(r'^create/',ItemCreateView.as_view(),name="item-create"),
    url(r'^(?P<pk>\w+)/',ItemDetailView.as_view(),name="item-detail"),
    url(r'^(?P<pk>\w+)/update/',ItemUpdateView.as_view(),name="item-update"),
    #url(r'^restaurant/mexican/$',MexicanRestaurantListView.as_view()),
]
