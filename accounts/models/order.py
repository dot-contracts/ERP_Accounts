from django.db.models import Q
from decimal import Decimal
from django.db import models

class Order(models.Model):
    wno = models.CharField(max_length=50)
    from_field = models.CharField(max_length=100)
    qty = models.IntegerField()
    cod = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    collected = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deficit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contract = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    received_by = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)

    @classmethod
    def clean_invalid_fields(cls):
        """
        Clean fields that contain invalid numeric values, like 'none'.
        """
        # Find orders where decimal fields have 'none' or other invalid string values
        invalid_orders = cls.objects.filter(
            Q(cod__exact='none') | 
            Q(contract__exact='none') | 
            Q(paid__exact='none') | 
            Q(qty__exact='none')
        )

        # Fix invalid entries by setting them to None or a default value
        for order in invalid_orders:
            if order.cod == 'none':
                order.cod = Decimal('0.00')  # Set to default 0.00 instead of None
            if order.contract == 'none':
                order.contract = Decimal('0.00')  # Set to default 0.00 instead of None
            if order.paid == 'none':
                order.paid = Decimal('0.00')  # Set to default 0.00 instead of None
            if order.qty == 'none':
                order.qty = 0  # Set quantity to 0 if it was invalid
            order.save()

