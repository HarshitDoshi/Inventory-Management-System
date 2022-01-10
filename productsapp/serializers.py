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
            "owner",
        ]


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
