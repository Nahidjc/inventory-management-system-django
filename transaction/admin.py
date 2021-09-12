from django.contrib import admin
from .models import PurchaseItem, SalesItem
# Register your models here.
admin.site.register(PurchaseItem)
admin.site.register(SalesItem)
