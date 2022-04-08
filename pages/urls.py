from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages, name='pages'),
    path('list/', views.List.as_view() , name='pages_list'),
    path('new/', views.New.as_view(), name='pages_new'),
    path('<int:pk>/', views.Detail.as_view() , name='pages_detail'),
    path('<int:pk>/edit/', views.Edit.as_view(), name='pages_edit'),
    path('<int:pk>/delete/', views.Delete.as_view(), name='pages_delete'),
]
