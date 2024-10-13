"""
URL configuration for crm_accounting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', accounts_views.login_view, name='login'),
    path('admin-dashboard/', accounts_views.admin_dashboard, name='admin_dashboard'),
    path('manager-dashboard/', accounts_views.manager_dashboard, name='manager_dashboard'),
    # path('employee-dashboard/', accounts_views.employee_dashboard, name='employee_dashboard'),
    path('upload-excel/', accounts_views.upload_excel, name='upload_excel'),
    path('manager-dashboard/', accounts_views.manager_dashboard, name='manager_dashboard'),
    path('submit-deposit/', accounts_views.submit_deposit, name='submit_deposit'),
]
