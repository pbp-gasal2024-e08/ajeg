from django import forms
from .models import Cart

class AddToCartForm(forms.ModelForm):  # Use ModelForm instead of Forms
    quantity = forms.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = Cart
        fields = ['quantity']  # Specify fields explicitly instead of '__all__' to avoid issues

    def save(self, commit=True):
        return super(AddToCartForm, self).save(commit=commit)

    def clean_password(self):
        return