from django.shortcuts import render
from .forms import PurchaseItemForm, SalesItemForm
from inventory.models import inventory
from django.shortcuts import HttpResponseRedirect, redirect
# Create your views here.


def itemPurchase(request):
    form = PurchaseItemForm()
    if request.method == 'POST':
        form = PurchaseItemForm(request.POST)
        if form.is_valid():
            form.save()
            inventoryID = request.POST.get('inventoryName')
            quantity = request.POST.get('quantity')
            # previous_units updated inventory
            inv_obj = inventory.objects.get(
                id=inventoryID)

            PreviousUnits = inv_obj.units

            updatedUnits = int(PreviousUnits) + int(quantity)
            print("Updated quantity", updatedUnits)
            # # updated_inventory
            inventory.objects.filter(
                id=inventoryID).update(units=updatedUnits)
            return redirect('home')

    return render(request, 'transaction/purchase.html', context={'form': form})


def salesItem(request):
    form = SalesItemForm()
    if request.method == 'POST':
        form = SalesItemForm(request.POST)
        if form.is_valid():
            form.save()
            inventoryID = request.POST.get('inventory_id')
            quantity = request.POST.get('quantity')

            # previous_units updated inventory
            inv_obj = inventory.objects.get(
                id=inventoryID)
            PreviousUnits = inv_obj.units

            updatedUnits = int(PreviousUnits) - int(quantity)
            print("Updated quantity", updatedUnits)
            # # updated_inventory
            inventory.objects.filter(
                id=inventoryID).update(units=updatedUnits)
            return redirect('home')

    return render(request, 'salesItem.html', context={'form': form})
