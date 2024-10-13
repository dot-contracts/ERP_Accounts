from django.db import models

class Order(models.Model):
    wno = models.CharField(max_length=50)
    from_field = models.CharField(max_length=100)
    qty = models.IntegerField()
    cod = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    collected = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deficit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contract = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid = models.CharField(max_length=50, null=True, blank=True)
    received_by = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.wno} - {self.from_field}"