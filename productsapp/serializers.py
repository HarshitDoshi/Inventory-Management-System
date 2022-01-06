from productsapp.models import Supplier, Category, Product, ProductOrder
from rest_framework import serializers


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Supplier
        fields = [
            "Supplier Name",
            "address",
            "phone",
            "email",
            "owner",
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Category
        fields = [
            "Category Name",
            "description",
            "owner",
        ]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = [
            "Product Name",
            "price",
            "Product Supplier",
            "Product Category",
            "owner",
        ]
        extra_kwargs = {
            'url': {'view_name': 'supplier-details', 'lookup_field': 'Supplier Name'},
            'Product Supplier': {'lookup_field': 'Supplier Name'}
        }


class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductOrder
        fields = [
            "customer_id",
            "product_id",
            "order_discount",
            "total_price",
            "order_date",
        ]
