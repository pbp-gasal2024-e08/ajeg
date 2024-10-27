from django.contrib import admin
from .models import Voucher

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ('code', 'expiry_date', 'is_claimed', 'is_flash_sale')
    search_fields = ('code',)

