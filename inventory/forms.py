from django import forms
from .models import inventory, createSupplier


class InventoryForm(forms.ModelForm):
    class Meta:
        model = inventory
        fields = ('name', 'units',)


class createSupplierForm(forms.ModelForm):
    class Meta:
        model = createSupplier
        fields = '__all__'
