from django.shortcuts import render
from .forms import PurchaseItemForm, SalesItemForm
from inventory.models import inventory
from transaction.models import SalesItem, PurchaseItem
from django.shortcuts import HttpResponseRedirect, redirect
from django.db.models import Avg, Count, Min, Sum
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
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
            return redirect('/transaction/item-dashboard/')

    return render(request, 'transaction/purchase.html', context={'form': form})


@login_required
def salesItem(request):
    form = SalesItemForm()
    error = ''
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

            if int(PreviousUnits) >= int(quantity):
                updatedUnits = int(PreviousUnits) - int(quantity)
                print("Updated quantity", updatedUnits)
                # # updated_inventory
                inventory.objects.filter(
                    id=inventoryID).update(units=updatedUnits)
                return redirect('/transaction/item-dashboard/')
            else:
                error = 'Your inventory stock is lower than sales quantity'

    return render(request, 'transaction/salesItem.html', context={'form': form, 'error': error})


@login_required
def item_dashboard(request):
    inventoryList = inventory.objects.all()
    product = SalesItem.objects.all()
    purchaseProducts = PurchaseItem.objects.all()
    saleProducts = SalesItem.objects.all()

    saleProducts = SalesItem.objects.all().values('inventory_id', 'inventory_id__name').order_by(
        'inventory_id').annotate(total_product=Sum('quantity'))

    print(product)

    return render(request, 'itemdashboard.html', context={'inventories': inventoryList, 'saleProducts': saleProducts, 'product': product, 'purchaseProducts': purchaseProducts})


@login_required
def bill_print(request, bill_id):
    print(bill_id)

    billDetails = SalesItem.objects.get(sale_id=bill_id)
    print(billDetails.totalPrice)
    return render(request, 'transaction/billprint.html', context={'billDetails': billDetails})


@login_required
def purchaseBill(request, bill_id):
    billDetails = PurchaseItem.objects.get(bill_id=bill_id)
    print(billDetails.bill_id)
    return render(request, 'transaction/purchaseBillprint.html', context={'billDetails': billDetails})


@login_required
def purchase_list(request):
    purchaseProducts = PurchaseItem.objects.all()
    print(purchaseProducts)
    return render(request, 'transaction/purchasesList.html', context={'purchaseProducts': purchaseProducts})


@login_required
def sales_item_lists(request):
    SalesItems = SalesItem.objects.all()
    return render(request, 'transaction/salesItemsLists.html', context={'SalesItems': SalesItems})
