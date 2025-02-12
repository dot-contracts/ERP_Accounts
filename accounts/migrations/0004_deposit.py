# Generated by Django 5.1.2 on 2024-10-10 14:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_branch_user_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_code', models.CharField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
