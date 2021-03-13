from typing import Counter
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
from allauth.account.signals import user_signed_up
from phonenumber_field.modelfields import PhoneNumberField 



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    member_since = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    street_address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    def __str__(self):
        return str(self.first_name)
    
    def get_phone_number(self):
        return self.phone_number
    
    @property  
    def get_full_address(self):
        return f"{self.street_address}, {self.city}, {self.country}, {self.zip_code}"
    
    @receiver(user_signed_up)
    def populate_profile(sociallogin, user, **kwargs):
        user.profile = Profile()
        user_data = user.socialaccount_set.filter(provider='google')[0].extra_data
        first_name = user_data['given_name']
        last_name = user_data['family_name']
        email = user_data['email']

        user.profile.first_name = first_name
        user.profile.last_name = last_name
        user.profile.email = email
        user.profile.save()
        
    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify("{obj.first_name}-{obj.last_name}".format(obj=self))
        super(Profile, self).save(*args, **kwargs)
        