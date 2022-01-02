from django.contrib import admin
from productsapp.models import Supplier, Category, Product, ProductOrder

admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOrder)
