from django.contrib.auth.models import User
from configuration.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


""" @api_view(["GET"])
def api_root(request, format=None) -> Response:
    return Response({
        "users": reverse("user-list", request=request, format=format),
        "products": reverse("productsapp:product-list", request=request, format=format),
        "customers": reverse("customersapp:customer-list", request=request, format=format),
        "customer-groups": reverse("customersapp:customergroup-list", request=request, format=format),
        "suppliers": reverse("productsapp:supplier-list", request=request, format=format),
        "product-categories": reverse("productsapp:category-list", request=request, format=format),
        "orders": reverse("productsapp:productorder-list", request=request, format=format),
    }); """


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
