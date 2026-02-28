from django.db import models
from django.apps import apps
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Room Choices
ROOM_CHOICES = [
    ('Living Room', 'Living Room'),
    ('Bedroom', 'Bedroom'),
    ('Kitchen', 'Kitchen'),
    ('Office', 'Office'),
    ('Dining Room', 'Dining Room'),
    ('Bathroom', 'Bathroom'),
    ('Home Office', 'Home Office'),
    ('Outdoor', 'Outdoor'),
]

# Furniture Type Choices
FURNITURE_TYPE_CHOICES = [
    ('Cots', 'Cots'),
    ('Sofa', 'Sofa'),
    ('Desk', 'Desk'),
    ('Wardrobe', 'Wardrobe'),
    ('Bed', 'Bed'),
    ('Chair', 'Chair'),
    ('Table', 'Table'),
    ('Cabinet', 'Cabinet'),
    ('Shelf', 'Shelf'),
    ('Bench', 'Bench'),
]

class MattressCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/mattress-categories/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Mattress Categories"

    def __str__(self):
        return self.name

class FurnitureCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/furniture-categories/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Furniture Categories"

    def __str__(self):
        return self.name

class BeddingCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/bedding-categories/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Bedding Categories"

    def __str__(self):
        return self.name

class SofaCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/sofa-categories/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sofa Categories"

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='products/brands/', blank=True, null=True)

    def __str__(self):
        return self.name

class Mattress(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        MattressCategory,
        on_delete=models.SET_NULL,
        related_name="mattresses",
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name="mattresses",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/mattresses/', blank=True, null=True)
    sizes = models.JSONField(
        default=list, 
        blank=True, 
        null=True,
        help_text='JSON format: [{"category": "Single", "dimensions": [{"size": "72 x 36", "price": 13500, "original_price": 18000}]}, ...]'
    )
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Mattresses"

    def __str__(self):
        return self.name

class Sofa(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        SofaCategory,
        on_delete=models.SET_NULL,
        related_name="sofas",
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name="sofas",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/sofas/', blank=True, null=True)
    pricing_info = models.CharField(max_length=100, default="Contact Salesman", help_text="Pricing information")
    sizes = models.JSONField(default=list, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Sofas"

    def __str__(self):
        return self.name

class Furniture(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        FurnitureCategory,
        on_delete=models.SET_NULL,
        related_name="furniture",
        null=True,
        blank=True,
    )
    furniture_type = models.CharField(max_length=100, blank=True, null=True, choices=FURNITURE_TYPE_CHOICES)
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name="furniture",
        null=True,
        blank=True,
    )
    material = models.CharField(max_length=200, blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField(default=0)
    customizable = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/furniture/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Furniture"

    def __str__(self):
        return self.name

class HomeUtility(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200)
    material = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='products/home-utilities/', blank=True, null=True)
    sizes = models.JSONField(default=list, blank=True, null=True)
    best_seller = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Home Utilities"

    def __str__(self):
        return self.name

class BeddingProduct(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        BeddingCategory,
        on_delete=models.SET_NULL,
        related_name="bedding_products",
        null=True,
        blank=True,
    )
    price = models.CharField(max_length=50, blank=True, null=True)
    discount = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='products/bedding/', blank=True, null=True)
    sizes = models.JSONField(
        default=list,
        blank=True,
        null=True,
        help_text='JSON format: [{"category": "Single", "dimensions": [{"size": "72 x 36", "price": 13500, "original_price": 18000}]}, ...]'
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class CustomFurniture(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/custom-furniture/', blank=True, null=True)
    tags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title

class InteriorApplication(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='products/interior-applications/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Interior Applications"

    def __str__(self):
        return self.name

class OrthopaedicMattress(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        MattressCategory,
        on_delete=models.SET_NULL,
        related_name="orthopaedic_mattresses",
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name="orthopaedic_mattresses",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/orthopaedic-mattresses/', blank=True, null=True)
    sizes = models.JSONField(
        default=list, 
        blank=True, 
        null=True,
        help_text='JSON format: [{"category": "Single", "dimensions": [{"size": "72 x 36", "price": 13500, "original_price": 18000}]}, ...]'
    )
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    doctor_recommended = models.BooleanField(default=True, help_text="Doctor recommended orthopaedic mattress")
    featured = models.BooleanField(default=False, help_text="Feature as prime product")

    class Meta:
        verbose_name_plural = "Orthopaedic Mattresses"

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_photo = models.ImageField(upload_to='products/testimonials/', blank=True, null=True)
    review = models.TextField()
    star_rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=5)
    product_photo = models.ImageField(upload_to='products/testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.customer_name} - {self.star_rating} stars"


def _iter_file_fields(model_class):
    for field in model_class._meta.fields:
        if isinstance(field, models.FileField):
            yield field


def _is_file_still_referenced(file_name, exclude_model=None, exclude_pk=None):
    products_app = apps.get_app_config('products')

    for model_class in products_app.get_models():
        for field in _iter_file_fields(model_class):
            query = {field.name: file_name}
            queryset = model_class.objects.filter(**query)

            if exclude_model is model_class and exclude_pk is not None:
                queryset = queryset.exclude(pk=exclude_pk)

            if queryset.exists():
                return True

    return False


@receiver(pre_save)
def delete_replaced_product_media_files(sender, instance, **kwargs):
    if sender._meta.app_label != 'products' or not instance.pk:
        return

    try:
        previous_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    for field in _iter_file_fields(sender):
        previous_file = getattr(previous_instance, field.name)
        current_file = getattr(instance, field.name)

        if not previous_file:
            continue

        previous_name = previous_file.name
        current_name = current_file.name if current_file else None

        if previous_name and previous_name != current_name:
            if not _is_file_still_referenced(previous_name, exclude_model=sender, exclude_pk=instance.pk):
                previous_file.storage.delete(previous_name)


@receiver(post_delete)
def delete_orphan_product_media_files(sender, instance, **kwargs):
    if sender._meta.app_label != 'products':
        return

    for field in _iter_file_fields(sender):
        file_obj = getattr(instance, field.name)

        if not file_obj:
            continue

        file_name = file_obj.name

        if file_name and not _is_file_still_referenced(file_name):
            file_obj.storage.delete(file_name)
