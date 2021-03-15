from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
import random

CATEGORY_CHOICES = (
    ('Beverage', 'Beverage'),
    ('Pasta','Pasta'),
    ('Cake','Cake'),
    ('Bakery','Bakery'),
    ('Sandwiches','Sandwiches'),
)

SIZES_CHOICES = (
    ('Short', 'Short'),
    ('Tall', 'Tall'),
    ('Grande', 'Grande'),
    ('Venti', 'Venti')
)

CAKE_CHOICES = (
    ('SLICE','SLICE'),
    ('WHOLE','WHOLE'),
)

def get_upload_path(instance, filename):
    return 'Items/{0}/{1}'.format(instance.name, filename)

def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))

class Item(models.Model):
    name = models.CharField(max_length=50)
    categories = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    sizes = models.CharField(choices=SIZES_CHOICES, max_length=50, null=True, blank=True, default="Short")
    cake_size = models.CharField(choices=CAKE_CHOICES, max_length=50, null=True, blank=True, default="SLICE")
    img = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    description = models.TextField()
    beverage_s_price = models.FloatField(null=True, blank=True)
    beverage_t_price = models.FloatField(null=True, blank=True)
    beverage_g_price = models.FloatField(null=True, blank=True)
    beverage_v_price = models.FloatField(null=True, blank=True)
    cake_slice_price = models.FloatField(null=True, blank=True)
    cake_whole_price = models.FloatField(null=True, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    available = models.BooleanField(default=True)
    slug= models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("featured-food", 
                       kwargs={"slug": self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })
    
    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })
        
    def get_add_to_cart_store_page_url(self):
        return reverse("add-to-cart-store-page", kwargs={
            'slug': self.slug
        })
    
    def get_remove_from_cart_store_page_url(self):
        return reverse("remove-from-cart-store-page", kwargs={
            'slug': self.slug
        })
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

class OrderItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity = models.IntegerField(default=1)
    category = models.CharField(max_length=50, null=True, blank=True)
    sizes = models.CharField(max_length=50, null=True, blank=True)
    cake_size = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(default=0,null=True, blank=True)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.item_quantity} of {self.item}"
    
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)
    ordered = models.BooleanField(default=False)
    reference_number = models.CharField(max_length=10, 
                                        null=True, blank=True, 
                                        unique=True, default=create_new_ref_number())
    
    
    def __str__(self):
        return self.reference_number
    