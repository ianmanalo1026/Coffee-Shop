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

def get_upload_path(instance, filename):
    return 'Items/{0}/{1}'.format(instance.title, filename)

def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))


class Item(models.Model):
    def get_price():
        pass
    
    name = models.CharField(max_length=50)
    categories = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    sizes = models.CharField(choices=SIZES_CHOICES, max_length=50, null=True, blank=True)
    img = models.ImageField(upload_to=None, null=True, blank=True)
    description = models.TextField()
    s_price = models.FloatField(null=True, blank=True)
    t_price = models.FloatField(null=True, blank=True)
    g_price = models.FloatField(null=True, blank=True)
    v_price = models.FloatField(null=True, blank=True)
    price = models.FloatField(default=get_price(), null=True, blank=True)
    slug= models.SlugField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("featured-food", kwargs={"slug": self.slug})
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)
    

class OrderItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity = models.IntegerField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.item_quantity} of {self.item}"
    
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    reference_number = models.CharField(max_length=10, null=True, blank=True, unique=True, default=create_new_ref_number())
    
    
    def __str__(self):
        return self.reference_number
    