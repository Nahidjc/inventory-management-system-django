from django import forms
from .models import inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = inventory
        fields = ('name', 'units',)
