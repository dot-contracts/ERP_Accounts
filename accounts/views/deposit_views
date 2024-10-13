from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Deposit

@login_required
def submit_deposit(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        transaction_code = request.POST['transaction_code']
        Deposit.objects.create(amount=amount, transaction_code=transaction_code)
        messages.success(request, 'Deposit recorded successfully.')
        return redirect('manager_dashboard')
    return render(request, 'deposit_form.html')