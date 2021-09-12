from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import InventoryForm, createSupplierForm
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
# Create your views here.


@login_required(login_url='/account/login')
def home(request):
    return render(request, 'dashboard.html', {})


def createInventory(request):
    form = InventoryForm()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'inventory/createInventory.html', context={'form': form})


def addSupplier(request):
    form = createSupplierForm()
    if request.method == 'POST':
        form = createSupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'inventory/addSupplier.html', context={'form': form})
