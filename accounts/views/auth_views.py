from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.role:
                if user.role.name == 'Admin':
                    return redirect('admin_dashboard')
                elif user.role.name == 'Branch Manager':
                    return redirect('manager_dashboard')
                elif user.role.name == 'Employee':
                    return redirect('employee_dashboard')
            else:
                messages.error(request, 'User role not assigned.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')