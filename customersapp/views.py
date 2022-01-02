from customersapp.models import Customer, CustomerGroup
from customersapp.serializers import CustomerSerializer, CustomerGroupSerializer
from rest_framework import generics


class CustomersList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerGroupsList(generics.ListCreateAPIView):
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer


class CustomerGroupDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer
