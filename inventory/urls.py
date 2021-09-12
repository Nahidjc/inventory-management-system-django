from django.urls import path, include
from inventory import views


app_name = "inventory"
urlpatterns = [
    path('create-inventory', views.createInventory, name='create-inventory')
]
