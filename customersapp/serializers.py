from customersapp.models import Customer, CustomerGroup
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'address', 'phone', 'email', 'group_id']

class CustomerGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerGroup
        fields = ['id', 'name']
