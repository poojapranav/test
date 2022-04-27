from django import forms
from .models import customer,orders
class customerform(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"
class orderform(forms.ModelForm):
    class Meta:
        model=orders
        fields="__all__"
