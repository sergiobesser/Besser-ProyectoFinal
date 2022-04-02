from django.urls import path
from .views import accounts, login, login_view

urlpatterns = [
    path('', accounts, name='accounts'),
    path('loginview', login_view, name='login_view'),
    path('login/', login, name='login'),
]
