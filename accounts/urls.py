import django
from django.urls import path
from .views import login, login_view, signup, signup_view, edit, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('loginview/', login_view, name='login_view'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('signupview/', signup_view, name='signup_view'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('edit/', edit, name='edit')
]
