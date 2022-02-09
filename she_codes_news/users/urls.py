from django.urls import path
from .views import CreateAccountView, CreateUserProfileView, HomePageView, get_user_profile

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('create-profile/', CreateUserProfileView.as_view(), name='createProfile'),
    path('home-page/', HomePageView.as_view(), name='homePage'),
    path('my/', get_user_profile, name='my'),
]
