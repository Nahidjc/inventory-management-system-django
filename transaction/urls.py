from django.urls import path, include
from transaction import views


app_name = "transaction"
urlpatterns = [
    path('purchase/', views.itemPurchase, name='purchase'),
    path('salesitem/', views.salesItem, name='salesitem'),
    path('item-dashboard/', views.item_dashboard, name='item-dashboard'),
    path('billprint/<bill_id>/', views.bill_print, name='bill-print'),
    path('purchase-lists/', views.purchase_list, name='purchase-list'),
    path('salesitem-lists/', views.sales_item_lists, name='sales-items-lists'),
]
