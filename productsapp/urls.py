from django.urls import path, include
from productsapp.views import (
    SupplierViewSet,
    CategoryViewSet,
    ProductViewSet,
    ProductOrderViewSet
)
from rest_framework.routers import DefaultRouter


app_name = "productsapp"

productsapp_router = DefaultRouter()
productsapp_router.register(r"products/categories", CategoryViewSet)
productsapp_router.register(r"products", ProductViewSet)
productsapp_router.register(r"suppliers", SupplierViewSet)
productsapp_router.register(r"orders", ProductOrderViewSet)
