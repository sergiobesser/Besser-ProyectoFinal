from django.urls import path
from .views import pages

urlpatterns = [
    path('pages/', pages, name='pages'),
]
