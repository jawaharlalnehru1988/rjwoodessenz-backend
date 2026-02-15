from django import forms
from django.contrib import admin
from .models import (
    MattressCategory, FurnitureCategory, BeddingCategory, SofaCategory,
    Brand, Mattress, Furniture, BeddingProduct, Sofa,
    HomeUtility, CustomFurniture, InteriorApplication, Testimonial, OrthopaedicMattress
)


MATTRESS_SIZE_CHOICES = [
    ("Single", "Single"),
    ("Double", "Double"),
    ("Queen", "Queen"),
    ("King", "King"),
]

SOFA_SIZE_CHOICES = [
    ("2-Seater", "2-Seater"),
    ("3-Seater", "3-Seater"),
    ("4-Seater", "4-Seater"),
    ("L-Shape", "L-Shape"),
    ("U-Shape", "U-Shape"),
]

HOME_UTILITY_SIZE_CHOICES = [
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
    ("Extra Large", "Extra Large"),
]


class MattressAdminForm(forms.ModelForm):
    sizes = forms.JSONField(
        required=False,
        help_text='Format: [{"category": "Single", "dimensions": [{"size": "72 x 36", "price": 13500, "original_price": 18000}]}]',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80})
    )

    class Meta:
        model = Mattress
        fields = "__all__"

class OrthopaedicMattressAdminForm(forms.ModelForm):
    sizes = forms.JSONField(
        required=False,
        help_text='Format: [{"category": "Single", "dimensions": [{"size": "72 x 36", "price": 13500, "original_price": 18000}]}]',
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80})
    )

    class Meta:
        model = OrthopaedicMattress
        fields = "__all__"

class SofaAdminForm(forms.ModelForm):
    sizes = forms.MultipleChoiceField(
        choices=SOFA_SIZE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Sofa
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and isinstance(self.instance.sizes, list):
            self.initial["sizes"] = self.instance.sizes

    def clean_sizes(self):
        return self.cleaned_data.get("sizes", [])

class HomeUtilityAdminForm(forms.ModelForm):
    sizes = forms.MultipleChoiceField(
        choices=HOME_UTILITY_SIZE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = HomeUtility
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and isinstance(self.instance.sizes, list):
            self.initial["sizes"] = self.instance.sizes

    def clean_sizes(self):
        return self.cleaned_data.get("sizes", [])

@admin.register(MattressCategory)
class MattressCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(FurnitureCategory)
class FurnitureCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BeddingCategory)
class BeddingCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SofaCategory)
class SofaCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Mattress)
class MattressAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'rating')
    list_filter = ('category', 'brand')
    search_fields = ('name', 'brand')
    form = MattressAdminForm
    fields = ('uid', 'category', 'brand', 'name', 'description', 'image', 'sizes', 'rating')

@admin.register(OrthopaedicMattress)
class OrthopaedicMattressAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'rating', 'doctor_recommended', 'featured')
    list_filter = ('category', 'brand', 'doctor_recommended', 'featured')
    search_fields = ('name', 'brand')
    form = OrthopaedicMattressAdminForm
    fields = ('uid', 'category', 'brand', 'name', 'description', 'image', 'sizes', 'rating', 'doctor_recommended', 'featured')

@admin.register(Sofa)
class SofaAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'pricing_info')
    list_filter = ('category', 'brand')
    search_fields = ('name', 'brand')
    form = SofaAdminForm
    fields = ('uid', 'category', 'brand', 'name', 'description', 'image', 'pricing_info', 'sizes', 'rating')

@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'furniture_type', 'price', 'brand')
    list_filter = ('category', 'furniture_type', 'brand')
    search_fields = ('name',)
    fields = ('uid', 'category', 'furniture_type', 'name', 'brand', 'material', 'size', 'price', 'discount', 'customizable', 'image')

@admin.register(BeddingProduct)
class BeddingProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name',)
    fields = ('uid', 'category', 'name', 'price', 'discount', 'image', 'description')

@admin.register(HomeUtility)
class HomeUtilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'material', 'best_seller')
    list_filter = ('category', 'best_seller')
    search_fields = ('name',)
    form = HomeUtilityAdminForm
    fields = ('uid', 'category', 'name', 'material', 'image', 'sizes', 'best_seller')

@admin.register(CustomFurniture)
class CustomFurnitureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(InteriorApplication)
class InteriorApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'star_rating', 'is_active', 'created_at')
    list_filter = ('star_rating', 'is_active', 'created_at')
    search_fields = ('customer_name', 'review')
    fields = ('customer_name', 'customer_photo', 'review', 'star_rating', 'product_photo', 'is_active')
    readonly_fields = ('created_at',)
