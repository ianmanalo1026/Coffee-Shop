from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.TextInput()
    street_address =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    province = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    def __init__(self, *args, **kw):
        super(ProfileForm, self).__init__(*args, **kw)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email
    
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "photo",
            "email",
            "phone_number",
            "street_address",
            "province",
            "city",
            "country",
            "zip_code",
        ]
        widgets = {
            'phone_number': forms.TextInput(attrs={'class':'form-control'})}