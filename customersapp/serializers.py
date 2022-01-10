from customersapp.models import Customer, CustomerGroup
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Customer
        fields = [
            "id",
            "First Name",
            "Last Name",
            "address",
            "phone",
            "email",
            "group_id",
            "owner",
        ]


class CustomerGroupSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = CustomerGroup
        fields = [
            "id",
            "customer_group_name",
            "owner",
        ]
