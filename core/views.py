from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from core.models import Item, OrderItem, Order
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView


def home(request):
    return HttpResponse('hello world')

class ItemListVIew(ListView):
    model = Item
    template_name = 'core/store.html'
    
class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/featured-food.html'
    

class OrderSummary(DetailView):
    model = Order
    template_name = 'core/cart.html'
    
    def get(self, request, *args, **kwargs):
        try:
            order = self.model.objects.get(
                customer=self.request.user, 
                ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 
                          self.template_name, context)
        except ObjectDoesNotExist:
            messages.error(self.request, 
                           "You do not have an active order")
            return redirect('store')
        
@login_required      
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        customer=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(customer=request.user, 
                                    ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.item_quantity += 1
            order_item.save()
            messages.success(request, 
                             "This item was updated to your cart."
                             )
        else:
            messages.success(request, 
                             "This item was added to your cart."
                             )
            order.items.add(order_item)
            order.save()
    else:
        order = Order.objects.create(
            customer=request.user)
        order.items.add(order_item)
        order.save()
        messages.success(request, 
                         "This item was added to your cart."
                         )
    return redirect("featured-food", slug=slug)


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        customer=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                customer=request.user,
                ordered=False
            )[0]
            if order_item.item_quantity > 1:
                order_item.item_quantity -= 1
                order_item.save()
            else:
                order = Order.objects.get(customer=request.user, 
                                          ordered=False)
                order.delete()
                order_item.delete()
            messages.info(request, 
                          "This item quantity was updated.")
            return redirect("featured-food", slug=slug)
        else:
            messages.info(request, 
                          "This item was not in your cart")
            return redirect("featured-food", slug=slug)
    else:
        messages.info(request, 
                      "You do not have an active order")
        return redirect("featured-food", slug=slug)