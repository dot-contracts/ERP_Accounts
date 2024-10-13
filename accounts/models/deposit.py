from django.db import models
from django.utils import timezone

class Deposit(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_code = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.transaction_code} - {self.amount}"