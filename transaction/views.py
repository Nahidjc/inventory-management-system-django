from django.shortcuts import render
from .forms import PurchaseItemForm
from inventory.models import inventory
from django.shortcuts import HttpResponseRedirect, redirect
# Create your views here.


def itemPurchase(request):
    form = PurchaseItemForm()
    if request.method == 'POST':
        form = PurchaseItemForm(request.POST)
        if form.is_valid():
            form.save()
            # inv = inventory()
            return redirect('home')

    return render(request, 'transaction/purchase.html', context={'form': form})
