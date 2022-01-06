from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from customersapp.models import Customer


class Supplier(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='suppliers',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name="Supplier Name",
        name="Supplier Name",
        db_column="supplier_name",
        max_length=512,
        blank=False,
        null=False,
    )
    address = models.TextField(
        blank=True,
        null=False,
    )
    phone = PhoneNumberField(
        blank=False,
        null=False,
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )

    class Meta:
        managed = True
        db_table = "supplier"
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"


class Category(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='categories',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name="Category Name",
        name="Category Name",
        db_column="category_name",
        max_length=512,
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=True,
        null=False,
    )

    class Meta:
        managed = True
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='products',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name="Product Name",
        name="Product Name",
        db_column="name",
        max_length=512,
        blank=False,
        null=False,
    )
    price = models.PositiveBigIntegerField(
        blank=False,
        null=False,
    )
    supplier_id = models.ForeignKey(
        to=Supplier,
        verbose_name="Product Supplier",
        name="Product Supplier",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    category_id = models.ForeignKey(
        to=Category,
        verbose_name="Product Category",
        name="Product Category",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    class Meta:
        managed = True
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductOrder(models.Model):
    customer_id = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    order_discount = models.IntegerField(blank=True, null=True)
    total_price = models.PositiveBigIntegerField(
        blank=False,
        null=False,
    )
    order_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    class Meta:
        managed = True
        db_table = 'product_order'
        verbose_name = "Product Order"
        verbose_name_plural = "Product Orders"
