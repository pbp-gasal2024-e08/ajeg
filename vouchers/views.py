from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import Voucher
from .forms import VoucherForm
from django.core import serializers
import json

from checkout.views import Cart

def voucher_list(request):
    vouchers = Voucher.objects.all()
    return render(request, 'voucher_list.html', {'vouchers': vouchers})

def claim_voucher(request, code):
    if request.method == 'POST':  # Pastikan ini adalah permintaan POST
        print(f"Claiming voucher with code: {code}")
        try:
            voucher = Voucher.objects.get(code=code)
            if not voucher.is_claimed and voucher.expiry_date > timezone.now():
                voucher.is_claimed = True
                voucher.save()
                return JsonResponse({'message': f'You successfully applied Code: {voucher.code} to your cart!', 'status': 'success'})
            return JsonResponse({'message': 'Voucher already claimed or expired.', 'status': 'error'})
        except Voucher.DoesNotExist:
            return JsonResponse({'message': 'Voucher not found.', 'status': 'error'})
        except Exception as e:  # Tangkap semua kesalahan lain
            print(f"Unexpected error: {str(e)}")  # Log kesalahan
            return JsonResponse({'message': 'An error occurred. Please try again.', 'status': 'error'})
    else:
        return JsonResponse({'message': 'Invalid request method.', 'status': 'error'})

def add_to_cart(request, code):
    if request.method == 'POST':
        try:
            # Cek apakah voucher dengan kode yang diberikan ada dan belum kadaluarsa
            voucher = Voucher.objects.get(code=code, is_claimed=True, expiry_date__gt=timezone.now())
            
            # Misalkan kamu memiliki model Cart untuk menyimpan voucher yang diklaim oleh pengguna
            # Pastikan kamu menggunakan user yang aktif saat ini, atau tambahkan logika lain
            cart, created = Cart.objects.get_or_create(user=request.user)  
            cart.vouchers.add(voucher)
            cart.save()
            
            return JsonResponse({'message': 'Voucher added to cart successfully!', 'status': 'success'})
        except Voucher.DoesNotExist:
            return JsonResponse({'message': 'Voucher not found or not claimed.', 'status': 'error'})
        except Exception as e:
            print(f"Unexpected error in add_to_cart: {str(e)}")
            return JsonResponse({'message': 'An error occurred while adding voucher to cart.', 'status': 'error'})
    else:
        return JsonResponse({'message': 'Invalid request method.', 'status': 'error'})


def voucher_list_json(request):
    vouchers = Voucher.objects.all()
    vouchers_json = serializers.serialize('json', vouchers)
    vouchers_data = json.loads(vouchers_json)
    return JsonResponse(vouchers_data, safe=False)
