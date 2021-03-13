from django.urls import path, include
from accounts.views import ProfileDetailView

app_name = 'accounts'

urlpatterns = [
    path('profile/<slug>', ProfileDetailView.as_view(), name='profile')
]
