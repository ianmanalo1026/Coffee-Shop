from django.urls import path, include
from .views import ItemListVIew, ItemDetailView, OrderSummary, home, add_to_cart, remove_from_cart

urlpatterns = [
    path('', home, name='home'),
    path('store/', ItemListVIew.as_view(), name='store'),
    path('cart/', OrderSummary.as_view(), name='cart'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('featured-food/<slug>/', ItemDetailView.as_view(), name='featured-food'),
]
