from productsapp.models import Supplier, Category, Product, ProductOrder
from rest_framework import serializers
from customersapp.models import Customer


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
            "id",
            "Product Name",
            "price",
            "owner",
        ]


class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    customer_id = serializers.HyperlinkedRelatedField(view_name="customersapp:customer-detail", queryset=Customer.objects.all())
    product_id = serializers.HyperlinkedRelatedField(view_name="productsapp:product-detail", queryset=Product.objects.all())
    class Meta:
        model = ProductOrder
        fields = [
            "id",
            "customer_id",
            "product_id",
            "order_discount",
            "total_price",
            "order_date",
        ]
