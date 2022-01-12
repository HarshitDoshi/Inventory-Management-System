from django.urls import path, include
from customersapp.views import (
    CustomerViewSet,
    CustomerGroupViewSet,
)
from rest_framework.routers import DefaultRouter


app_name = "customersapp"

customersapp_router = DefaultRouter()
customersapp_router.register(r"customers/groups", CustomerGroupViewSet)
customersapp_router.register(r"customers", CustomerViewSet)
