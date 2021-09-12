from django.db import models
from inventory.models import inventory, createSupplier
# Create your models here.


class PurchaseItem(models.Model):
    bill_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(
        createSupplier, on_delete=models.CASCADE, related_name='purchasesupplier')
    inventoryName = models.ForeignKey(inventory, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    itemPrice = models.PositiveIntegerField(default=1)
    quantity = models.IntegerField(default=1)
    totalPrice = models.IntegerField(default=1)

    def __str__(self):
        return self.inventoryName + ' ' + self.quantity
