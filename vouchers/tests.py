from django.test import TestCase
from .models import Voucher
from django.utils import timezone

class VoucherModelTest(TestCase):

    def setUp(self):
        self.voucher = Voucher.objects.create(
            code='AJEG20',
            discount_percentage=20,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=30),
            description='Discount 20%'
        )

    def test_voucher_str(self):
        self.assertEqual(str(self.voucher), 'AJEG20')

    def test_voucher_validity(self):
        self.assertTrue(self.voucher.start_date <= timezone.now() <= self.voucher.end_date)
