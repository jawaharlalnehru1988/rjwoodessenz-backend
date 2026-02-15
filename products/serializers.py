from rest_framework import serializers
from .models import (
    MattressCategory, FurnitureCategory, BeddingCategory, SofaCategory,
    Brand, Mattress, Furniture, BeddingProduct, Sofa,
    HomeUtility, CustomFurniture, InteriorApplication, Testimonial, OrthopaedicMattress
)

class MattressCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MattressCategory
        fields = '__all__'

class FurnitureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureCategory
        fields = '__all__'

class BeddingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BeddingCategory
        fields = '__all__'

class SofaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SofaCategory
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class MattressSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    
    class Meta:
        model = Mattress
        fields = '__all__'

class SofaSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    
    class Meta:
        model = Sofa
        fields = '__all__'

class FurnitureSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    
    class Meta:
        model = Furniture
        fields = '__all__'

class BeddingProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = BeddingProduct
        fields = '__all__'

class HomeUtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeUtility
        fields = '__all__'

class CustomFurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFurniture
        fields = '__all__'

class InteriorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorApplication
        fields = '__all__'

class OrthopaedicMattressSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    
    class Meta:
        model = OrthopaedicMattress
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
