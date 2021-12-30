from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomerGroup(models.Model):
    name = models.CharField(
        verbose_name="Customer Group Name",
        name="Customer Group Name",
        db_column="name",
        max_length=512,
    )

    class Meta:
        managed = True
        db_table = "customer_group"


class Customer(models.Model):
    first_name = models.CharField(
        verbose_name="First Name",
        name="First Name",
        db_column="first_name",
        max_length=512,
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        name="Last Name",
        db_column="last_name",
        max_length=512,
    )
    address = models.TextField()
    phone = PhoneNumberField()
    email = models.EmailField()
    group_id = models.ForeignKey(to=CustomerGroup, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "customer"
