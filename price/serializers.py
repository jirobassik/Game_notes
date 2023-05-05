from rest_framework import serializers
from djmoney.contrib.django_rest_framework import MoneyField

class GamePriceSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, write_only=True)
    name = serializers.CharField(max_length=70, allow_null=False, allow_blank=False)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency="USD",)
    game = serializers.IntegerField(required=True)
    price_currency = serializers.CharField(allow_null=True, allow_blank=True, required=False)

