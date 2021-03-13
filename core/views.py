from django.shortcuts import render
from django.http import HttpResponse
from core.models import Item
from django.views.generic import ListView, DetailView


def home(request):
    return HttpResponse('hello world')

class ItemListVIew(ListView):
    model = Item
    template_name = 'core/store.html'
    
class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/featured-food.html'