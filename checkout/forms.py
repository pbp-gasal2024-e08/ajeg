from math import prod
from typing import Any
from django import forms

from myauth.models import AjegUser

from .models import Cart
from main.models import Product

class AddToCartForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=AjegUser.objects.all(), empty_label=None)
    # product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1, max_value=100)
    # total_price = forms.IntegerField()



    class Meta:
        model = Cart
        fields = ['quantity']

    def save(self, commit = True):
        cart = super(AddToCartForm, self).save()
        # if commit:
        #     Cart.objects.create(
        #         user = self.user,
        #         product = self.product,
        #         quantity = self.cleaned_data['quantity'],
        #         total_price = self.product.price * self.cleaned_data['quantity']
        #     )
        return cart