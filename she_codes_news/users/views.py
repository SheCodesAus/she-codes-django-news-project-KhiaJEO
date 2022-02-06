
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic 
from .models import CustomUser
from .forms import CustomUserCreationForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class CreateUserProfileView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('profile')
    template_name = 'users/userProfileForm.html'
