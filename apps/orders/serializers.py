from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.orders.models import OrderItem, Order
from apps.products.models import Product


class OrderedItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')


class OrderCreateSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    ordered_items = serializers.ListField(
        child=OrderedItemSerializer(),
        allow_empty=False,
        max_length=20
    )

    def validate(self, data):
        validation_errors = {'ordered_items': dict()}
        for item in data['ordered_items']:
            if item['quantity'] > item['product'].stock_quantity:
                validation_errors['ordered_items'][item['product'].id] = 'Available product quantity is exceeded'

        if validation_errors['ordered_items']:
            raise ValidationError(validation_errors)
        return data

    @transaction.atomic()
    def create(self, validated_data):
        order_obj = Order.objects.create(user=validated_data['user'])

        order_items_to_create = []
        for order_item_data in validated_data['ordered_items']:
            product_obj = order_item_data['product']
            product_obj.stock_quantity -= order_item_data['quantity']
            product_obj.save()
            order_items_to_create.append(OrderItem(order=order_obj, **order_item_data))

        OrderItem.objects.bulk_create(order_items_to_create)
        return validated_data

    class Meta:
        model = OrderItem
        fields = ('ordered_items',)


class OrderListSerializer(serializers.ModelSerializer):
    items = OrderedItemSerializer(source='ordered_items', many=True)

    class Meta:
        model = Order
        fields = ('id', 'datetime', 'items')
