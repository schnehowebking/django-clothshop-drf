from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_popularity(self, obj):
        return obj.get_popularity()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):
    items = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = WishList
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    items = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'
