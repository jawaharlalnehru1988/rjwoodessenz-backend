"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from products.views import (
    MattressCategoryViewSet, FurnitureCategoryViewSet, BeddingCategoryViewSet, SofaCategoryViewSet,
    BrandViewSet, MattressViewSet, FurnitureViewSet, SofaViewSet,
    BeddingProductViewSet, HomeUtilityViewSet,
    CustomFurnitureViewSet, InteriorApplicationViewSet, OrthopaedicMattressViewSet
)
from users.views import UserViewSet, UserProfileViewSet, UserRegisterView, UserLoginView
from testimonials.views import TestimonialViewSet

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
router.register(r'users', UserViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'testimonials', TestimonialViewSet)

# Customize Django admin site
admin.site.site_header = "RJ Wood Essenz Admin"
admin.site.site_title = "RJ Wood Essenz Admin Portal"
admin.site.index_title = "Welcome to RJ Wood Essenz Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', UserRegisterView.as_view(), name='user-register'),
    path('api/auth/login/', UserLoginView.as_view(), name='user-login'),
    path('api/', include(router.urls)),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
