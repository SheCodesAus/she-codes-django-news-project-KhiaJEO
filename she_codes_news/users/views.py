
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views import generic 
from .models import CustomUser
from .forms import CustomUserCreationForm, CreateUserProfileForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.views.generic import DetailView, ListView
from news.models import NewsStory


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:createProfile')
    template_name = 'users/createAccount.html'

    def form_valid(self, form):
        f=super().form_valid(form)
        user = self.object
        login(self.request, user)
        return f

class CreateUserProfileView(UpdateView):
    form_class = CreateUserProfileForm
    success_url = reverse_lazy('users:homePage')
    template_name = 'users/userProfileForm.html'
    
    def get_success_url(self):
        print(self.request.user.id)
        print(type(self.get_form()))
        return reverse_lazy('users:yourprofile', kwargs={"pk":self.request.user.id})

    def get_object(self):
        return self.request.user

class YourProfile(generic.DetailView):
    model = CustomUser
    template_name = 'users/yourprofile.html'


# View by author
class AuthorsView(ListView):
    # model = CustomUser
    template_name = 'users/authors.html'
    # context_object_name = 'authors'

    def get_queryset(self):
        self.authors = get_object_or_404(CustomUser, name=self.kwargs['authors'])
        return NewsStory.objects.filter(authors=self.authors)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = self.authors
        return context

    


    