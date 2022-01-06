from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from productsapp.views import SupplierList, SupplierDetail, CategoryList, CategoryDetail, ProductList, ProductDetail, ProductOrderList, ProductOrderDetail

app_name = "productsapp"
urlpatterns = [
    path("suppliers/", SupplierList.as_view()),
    path("suppliers/<int:pk>", SupplierDetail.as_view()),
    path("products/", ProductList.as_view()),
    path("products/<int:pk>", ProductDetail.as_view()),
    path("products/categories/", CategoryList.as_view()),
    path("products/categories/<int:pk>", CategoryDetail.as_view()),
    path("orders/", ProductOrderList.as_view()),
    path("orders/<int:pk>", ProductOrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
