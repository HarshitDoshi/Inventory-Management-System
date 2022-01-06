from customersapp.models import Customer, CustomerGroup
from customersapp.serializers import CustomerSerializer, CustomerGroupSerializer
from rest_framework import generics


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerGroupList(generics.ListCreateAPIView):
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer


class CustomerGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer
