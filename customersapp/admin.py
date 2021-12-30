from django.contrib import admin
from .models import Customer, CustomerGroup


admin.site.register(Customer, CustomerGroup)
