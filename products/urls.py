from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, MattressViewSet, FurnitureViewSet, 
    BeddingProductViewSet, SpecialProductViewSet, 
    CustomFurnitureViewSet, HeavyDutyProductViewSet, NewArrivalViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'mattresses', MattressViewSet)
router.register(r'furniture', FurnitureViewSet)
router.register(r'bedding', BeddingProductViewSet)
router.register(r'special-products', SpecialProductViewSet)
router.register(r'custom-furniture', CustomFurnitureViewSet)
router.register(r'heavy-duty', HeavyDutyProductViewSet)
router.register(r'new-arrivals', NewArrivalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
