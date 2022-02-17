from django.urls import path
from .views import CreateAccountView, CreateUserProfileView, YourProfile, AuthorsView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('create-profile/', CreateUserProfileView.as_view(), name='createProfile'),
    path('<int:pk>', YourProfile.as_view(), name='yourprofile'),
    path('authors/', AuthorsView.as_view(), name='authors'),
]
