from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_list, name='data_list'),
    path('swimmer/<int:pk>', views.swimmer_detail, name='swimmer_detail')
]
