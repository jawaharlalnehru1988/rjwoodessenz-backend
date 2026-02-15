from django.db import models
from django.contrib.auth.models import User

# User Type Choices
USER_TYPE_CHOICES = [
    ('product_buyer', 'Product Buying User'),
    ('inquiry_maker', 'Inquiry Making User'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    # Fields for product buying users
    delivery_address_line1 = models.CharField(max_length=255, blank=True, null=True, help_text="Street address, P.O. box")
    delivery_address_line2 = models.CharField(max_length=255, blank=True, null=True, help_text="Apartment, suite, unit, building, floor, etc.")
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

    def get_full_address(self):
        """Returns formatted delivery address"""
        if not self.delivery_address_line1:
            return "No address provided"
        
        address_parts = [self.delivery_address_line1]
        if self.delivery_address_line2:
            address_parts.append(self.delivery_address_line2)
        address_parts.extend([
            self.city,
            self.state,
            self.postal_code,
            self.country
        ])
        return ", ".join(filter(None, address_parts))
