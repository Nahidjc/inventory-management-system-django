from django import forms
from .models import PurchaseItem, SalesItem


class PurchaseItemForm(forms.ModelForm):

    class Meta:
        model = PurchaseItem
        fields = '__all__'


class SalesItemForm(forms.ModelForm):
    class Meta:
        model = SalesItem
        fields = '__all__'
