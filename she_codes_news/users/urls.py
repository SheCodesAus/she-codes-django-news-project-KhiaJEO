from django.urls import path
from .views import CreateAccountView
from .views import CreateUserProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('create-profile/', CreateUserProfileView.as_view(), name='createProfile'),
]