from django.urls import path, include
from .views import (ItemListVIew,
                    ItemDetailView,
                    OrderSummary,
                    home,
                    add_to_cart,
                    remove_from_cart,
                    remove_from_cart_store_page,
                    add_to_cart_store_page
                    )

urlpatterns = [
    path('', home, name='home'),
    path('store/', ItemListVIew.as_view(), name='store'),
    path('cart/', OrderSummary.as_view(), name='cart'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('add-to-cart-store-page/<slug>/', add_to_cart_store_page, name='add-to-cart-store-page'),
    path('remove-from-cart-store-page/<slug>/', remove_from_cart_store_page, name='remove-from-cart-store-page'),
    path('featured-food/<slug>/', ItemDetailView.as_view(), name='featured-food'),
]
