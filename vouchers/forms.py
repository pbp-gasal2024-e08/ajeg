from django import forms
from .models import Voucher

class VoucherForm(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = ['code', 'discount', 'expiry_date']

