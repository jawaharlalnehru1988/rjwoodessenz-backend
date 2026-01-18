from rest_framework import serializers
from .models import (
    Category, Mattress, Furniture, BeddingProduct, 
    SpecialProduct, CustomFurniture, HeavyDutyProduct, NewArrival
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MattressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mattress
        fields = '__all__'

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'

class BeddingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeddingProduct
        fields = '__all__'

class SpecialProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialProduct
        fields = '__all__'

class CustomFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFurniture
        fields = '__all__'

class HeavyDutyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeavyDutyProduct
        fields = '__all__'

class NewArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewArrival
        fields = '__all__'
