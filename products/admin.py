from django.contrib import admin
from .models import (
    Category, Mattress, Furniture, BeddingProduct, 
    SpecialProduct, CustomFurniture, HeavyDutyProduct, NewArrival
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Mattress)
class MattressAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'base_price', 'discount_percent')
    search_fields = ('name', 'brand')

@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('name', 'furniture_type', 'room', 'price', 'brand')
    list_filter = ('furniture_type', 'room', 'brand')
    search_fields = ('name', 'brand')

@admin.register(BeddingProduct)
class BeddingProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(SpecialProduct)
class SpecialProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'best_seller')
    list_filter = ('category', 'brand', 'best_seller')

@admin.register(CustomFurniture)
class CustomFurnitureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(HeavyDutyProduct)
class HeavyDutyProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)

@admin.register(NewArrival)
class NewArrivalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
