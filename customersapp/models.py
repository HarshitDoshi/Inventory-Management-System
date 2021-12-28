from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomerGroup(models.Model):
    name = models.CharField(
        verbose_name="Customer Group Name",
        name="Customer Group Name",
        db_column="name"
    )


class Customer(models.Model):
    first_name = models.CharField(
        verbose_name="First Name",
        name="First Name",
        db_column="first_name",
    )
    last_name = models.CharField(
        verbose_name="Last Name",
        name="Last Name",
        db_column="last_name",
    )
    address = models.TextField()
    phone = PhoneNumberField()
    email = models.EmailField()
    group_id = models.ForeignKey(to=CustomerGroup)
