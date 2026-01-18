from rest_framework import viewsets
from .models import (
    Category, Mattress, Furniture, BeddingProduct, 
    SpecialProduct, CustomFurniture, HeavyDutyProduct, NewArrival
)
from .serializers import (
    CategorySerializer, MattressSerializer, FurnitureSerializer, 
    BeddingProductSerializer, SpecialProductSerializer, 
    CustomFurnitureSerializer, HeavyDutyProductSerializer, NewArrivalSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class MattressViewSet(viewsets.ModelViewSet):
    queryset = Mattress.objects.all()
    serializer_class = MattressSerializer
    lookup_field = 'uid'

class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    lookup_field = 'uid'

class BeddingProductViewSet(viewsets.ModelViewSet):
    queryset = BeddingProduct.objects.all()
    serializer_class = BeddingProductSerializer
    lookup_field = 'uid'

class SpecialProductViewSet(viewsets.ModelViewSet):
    queryset = SpecialProduct.objects.all()
    serializer_class = SpecialProductSerializer
    lookup_field = 'uid'

class CustomFurnitureViewSet(viewsets.ModelViewSet):
    queryset = CustomFurniture.objects.all()
    serializer_class = CustomFurnitureSerializer
    lookup_field = 'uid'

class HeavyDutyProductViewSet(viewsets.ModelViewSet):
    queryset = HeavyDutyProduct.objects.all()
    serializer_class = HeavyDutyProductSerializer
    lookup_field = 'uid'

class NewArrivalViewSet(viewsets.ModelViewSet):
    queryset = NewArrival.objects.all()
    serializer_class = NewArrivalSerializer
    lookup_field = 'uid'
