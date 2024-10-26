from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import Voucher
from .forms import VoucherForm
from django.core import serializers
import json

def voucher_list(request):
    vouchers = Voucher.objects.all()
    return render(request, 'voucher_list.html', {'vouchers': vouchers})

def claim_voucher(request, code):
    if request.method == 'POST':  # Ensure it's a POST request
        form = VoucherForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                voucher = Voucher.objects.get(code=code)
                if not voucher.is_claimed and voucher.expiry_date > timezone.now():
                    voucher.is_claimed = True
                    voucher.save()
                    return JsonResponse({'message': f'You successfully applied Code: {voucher.code} to your cart!', 'status': 'success'})
                return JsonResponse({'message': 'Voucher already claimed or expired.', 'status': 'error'})
            except Voucher.DoesNotExist:
                return JsonResponse({'message': 'Voucher not found.', 'status': 'error'})
        else:
            return JsonResponse({'message': 'Invalid form data.', 'status': 'error', 'errors': form.errors})
    else:
        return JsonResponse({'message': 'Invalid request method.', 'status': 'error'})
    

def voucher_list_json(request):
    vouchers = Voucher.objects.all()
    vouchers_json = serializers.serialize('json', vouchers)
    vouchers_data = json.loads(vouchers_json)
    return JsonResponse(vouchers_data, safe=False)
