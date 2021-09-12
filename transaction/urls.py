from django.urls import path, include
from transaction import views


app_name = "inventory_app"
urlpatterns = [
    path('purchase/', views.itemPurchase, name='purchase'),
]
