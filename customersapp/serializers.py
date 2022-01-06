from customersapp.models import Customer, CustomerGroup
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
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
            "name",
            "owner",
        ]
