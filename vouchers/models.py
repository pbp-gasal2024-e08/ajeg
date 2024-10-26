from django.db import models

class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    expiry_date = models.DateTimeField()
    is_claimed = models.BooleanField(default=False)
    is_flash_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code} - {self.discount}% oFF"
