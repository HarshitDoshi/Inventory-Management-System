from productsapp.models import Supplier, Category, Product, ProductOrder
from rest_framework import serializers


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            "name",
            "address",
            "phone",
            "email",
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name",
            "description",
        ]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "supplier_id",
            "category_id",
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
