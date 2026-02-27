from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    fields = ('user_type', 'phone', 'delivery_address_line1', 'delivery_address_line2', 
              'city', 'state', 'postal_code', 'country', 'share_location')


class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_user_type', 'get_phone', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'profile__user_type')
    
    def get_user_type(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.get_user_type_display()
        return '-'
    get_user_type.short_description = 'User Type'
    
    def get_phone(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.phone or '-'
        return '-'
    get_phone.short_description = 'Phone'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


# Unregister the default User admin
admin.site.unregister(User)

# Register User with the custom admin
admin.site.register(User, CustomUserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'phone', 'city', 'created_at')
    list_filter = ('user_type', 'country', 'state')
    search_fields = ('user__username', 'user__email', 'phone', 'city', 'share_location')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'user_type', 'phone')
        }),
        ('Delivery Address (For Product Buyers)', {
            'fields': ('delivery_address_line1', 'delivery_address_line2', 'city', 
                      'state', 'postal_code', 'country', 'share_location'),
            'description': 'These fields are required only for Product Buying Users'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
