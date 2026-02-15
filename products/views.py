from rest_framework import viewsets
from .models import (
    MattressCategory, FurnitureCategory, BeddingCategory, SofaCategory,
    Brand, Mattress, Furniture, BeddingProduct, Sofa,
    HomeUtility, CustomFurniture, InteriorApplication, Testimonial, OrthopaedicMattress
)
from .serializers import (
    MattressCategorySerializer, FurnitureCategorySerializer, BeddingCategorySerializer, SofaCategorySerializer,
    BrandSerializer, MattressSerializer, FurnitureSerializer, SofaSerializer,
    BeddingProductSerializer, HomeUtilitySerializer,
    CustomFurnitureSerializer, InteriorApplicationSerializer, TestimonialSerializer, OrthopaedicMattressSerializer
)

class MattressCategoryViewSet(viewsets.ModelViewSet):
    queryset = MattressCategory.objects.all()
    serializer_class = MattressCategorySerializer
    lookup_field = 'slug'

class FurnitureCategoryViewSet(viewsets.ModelViewSet):
    queryset = FurnitureCategory.objects.all()
    serializer_class = FurnitureCategorySerializer
    lookup_field = 'slug'

class BeddingCategoryViewSet(viewsets.ModelViewSet):
    queryset = BeddingCategory.objects.all()
    serializer_class = BeddingCategorySerializer
    lookup_field = 'slug'

class SofaCategoryViewSet(viewsets.ModelViewSet):
    queryset = SofaCategory.objects.all()
    serializer_class = SofaCategorySerializer
    lookup_field = 'slug'

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'

class MattressViewSet(viewsets.ModelViewSet):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer
    lookup_field = 'uid'

class SofaViewSet(viewsets.ModelViewSet):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer
    lookup_field = 'uid'

class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    lookup_field = 'uid'

class BeddingProductViewSet(viewsets.ModelViewSet):
    queryset = BeddingProduct.objects.all()
    serializer_class = BeddingProductSerializer
    lookup_field = 'uid'

class HomeUtilityViewSet(viewsets.ModelViewSet):
    queryset = HomeUtility.objects.all()
    serializer_class = HomeUtilitySerializer
    lookup_field = 'uid'

class CustomFurnitureViewSet(viewsets.ModelViewSet):
    queryset = CustomFurniture.objects.all()
    serializer_class = CustomFurnitureSerializer
    lookup_field = 'uid'

class InteriorApplicationViewSet(viewsets.ModelViewSet):
    queryset = InteriorApplication.objects.all()
    serializer_class = InteriorApplicationSerializer
    lookup_field = 'uid'

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer

class OrthopaedicMattressViewSet(viewsets.ModelViewSet):
    queryset = OrthopaedicMattress.objects.all()
    serializer_class = OrthopaedicMattressSerializer
    lookup_field = 'uid'
