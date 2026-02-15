from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Testimonial(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_photo = models.ImageField(upload_to='testimonials/customers/', blank=True, null=True)
    review = models.TextField()
    star_rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    )
    product_photo = models.ImageField(upload_to='testimonials/products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, help_text="Display this testimonial on the website")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"{self.customer_name} - {self.star_rating} stars"
