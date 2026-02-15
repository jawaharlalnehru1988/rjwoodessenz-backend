from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MattressCategoryViewSet, FurnitureCategoryViewSet, BeddingCategoryViewSet, SofaCategoryViewSet,
    BrandViewSet, MattressViewSet, FurnitureViewSet, SofaViewSet,
    BeddingProductViewSet, HomeUtilityViewSet,
    CustomFurnitureViewSet, InteriorApplicationViewSet, TestimonialViewSet, OrthopaedicMattressViewSet
)

router = DefaultRouter()
router.register(r'mattress-categories', MattressCategoryViewSet)
router.register(r'furniture-categories', FurnitureCategoryViewSet)
router.register(r'bedding-categories', BeddingCategoryViewSet)
router.register(r'sofa-categories', SofaCategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'mattresses', MattressViewSet)
router.register(r'orthopaedic-mattresses', OrthopaedicMattressViewSet)
router.register(r'sofas', SofaViewSet)
router.register(r'furniture', FurnitureViewSet)
router.register(r'bedding', BeddingProductViewSet)
router.register(r'home-utilities', HomeUtilityViewSet)
router.register(r'custom-furniture', CustomFurnitureViewSet)
router.register(r'interior-applications', InteriorApplicationViewSet)
router.register(r'testimonials', TestimonialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
