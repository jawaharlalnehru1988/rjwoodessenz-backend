from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'star_rating', 'is_active', 'created_at']
    list_filter = ['star_rating', 'is_active', 'created_at']
    search_fields = ['customer_name', 'review']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_name', 'customer_photo')
        }),
        ('Review Details', {
            'fields': ('review', 'star_rating', 'product_photo')
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )
