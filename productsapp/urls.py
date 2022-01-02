from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from productsapp.views import SuppliersList, SupplierDetails, CategoriesList, CategoryDetails, ProductsList, ProductDetails, ProductOrdersList, ProductOrderDetails


urlpatterns = [
    path("suppliers/", SuppliersList.as_view()),
    path("suppliers/<int:pk>", SupplierDetails.as_view()),
    path("products/", ProductsList.as_view()),
    path("products/<int:pk>", ProductDetails.as_view()),
    path("products/categories/", CategoriesList.as_view()),
    path("products/categories/<int:pk>", CategoryDetails.as_view()),
    path("orders/", ProductOrdersList.as_view()),
    path("orders/<int:pk>", ProductOrderDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
