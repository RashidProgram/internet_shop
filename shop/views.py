from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Shop


class TovarsListView(ListView):
    template_name = 'shop/list.html'
    model = Shop
    context_object_name = 'tovars'


class TovarsDetailView(DetailView):
    template_name = 'shop/detail.html'
    model = Shop
    context_object_name = 'tovar'
    queryset = Shop.objects.all()
