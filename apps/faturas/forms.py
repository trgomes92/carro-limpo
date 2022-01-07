from django import forms

from .models import Fatura

class FaturaForm(forms.ModelForm):
    class Meta:
        model = Fatura
        exclude = ('user', 'data', 'pago')

class FaturaEditForm(forms.ModelForm):
    class Meta:
        model = Fatura
        fields = ('pago',)