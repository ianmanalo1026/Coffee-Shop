from django.urls import path, include
from .views import ItemListVIew, ItemDetailView, home

urlpatterns = [
    path('', home, name='home'),
    path('store/', ItemListVIew.as_view(), name='store'),
    path('featured-food/<slug>', ItemDetailView.as_view(), name='featured-food'),
]
