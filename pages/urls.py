from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages, name='pages'),
    path('list/', views.List.as_view() , name='pages_list'),
    path('detail/', views.Detail.as_view() , name='pages_detail'),
    # path('new/', new_page, name='new_page'),
    path('edit/', views.Edit.as_view(), name='pages_edit'),
    path('delete/', views.Delete.as_view(), name='pages_delete'),
]
