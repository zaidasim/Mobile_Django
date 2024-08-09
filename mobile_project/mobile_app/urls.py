from django.urls import path
from .views import item_list_create
from . import views

urlpatterns = [
    path('items/',item_list_create,name='item-list-create'),
    
    path('test/', views.test_view, name='test_view'),

]
  