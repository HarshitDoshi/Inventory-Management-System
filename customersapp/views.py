from customersapp.models import Customer, CustomerGroup
from customersapp.serializers import CustomerSerializer, CustomerGroupSerializer
from rest_framework import generics, permissions, viewsets
from customersapp.permissions import IsOwnerOrReadOnly


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CustomerGroupViewSet(viewsets.ModelViewSet):
    queryset = CustomerGroup.objects.all()
    serializer_class = CustomerGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
