from django.urls import path
from .views import accounts

urlpatterns = [
    path('accounts/', accounts, name='accounts'),
]
