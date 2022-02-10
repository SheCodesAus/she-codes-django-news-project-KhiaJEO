
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views import generic 
from .models import CustomUser
from .forms import CustomUserCreationForm, CreateUserProfileForm
from django.shortcuts import render
from news.models import NewsStory 


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:createProfile')
    template_name = 'users/createAccount.html'

class CreateUserProfileView(FormView):
    form_class = CreateUserProfileForm
    success_url = reverse_lazy('users:homePage')
    template_name = 'users/userProfileForm.html'

class HomePageView(generic.DetailView):
    model = CustomUser
    template_name = 'users/homePageView.html'

def get_user_profile(request):
    user = request.user
    stories = NewsStory.objects.filter(author=request.user.id)
    return render(request, 'users/homePageView.html', {"user": request.user, "stories": stories})
    