from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomerGroup(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='customer_groups',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    name = models.CharField(
        verbose_name="Customer Group Name",
        name="customer_group_name",
        db_column="name",
        max_length=512,
        blank=False,
        null=False,
    )

    class Meta:
        managed = True
        db_table = "customer_group"
        verbose_name = "Customer Group"
        verbose_name_plural = "Customer Groups"


class Customer(models.Model):
    owner = models.ForeignKey(
        'auth.User',
        related_name='customers',
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        verbose_name="First Name",
        name="First Name",
        db_column="first_name",
        max_length=512,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        name="Last Name",
        db_column="last_name",
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
    group_id = models.ForeignKey(
        to=CustomerGroup,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    class Meta:
        managed = True
        db_table = "customer"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
