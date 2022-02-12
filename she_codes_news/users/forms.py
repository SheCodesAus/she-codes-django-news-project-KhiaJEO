from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta: 
        model = CustomUser
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class CreateUserProfileForm(forms.ModelForm):
    avatar = forms.URLField(required=False)
    Your_socials = forms.URLField(required=False)
    Location = forms.CharField(max_length=50, required=False, help_text='Where are you writing from?')
    About_you = forms.CharField(widget=forms.Textarea, max_length=500, required=False, help_text='Tell us about yourself :-)')

    class Meta:
        model = CustomUser
        fields = ['Your_socials', 'Location', 'About_you']