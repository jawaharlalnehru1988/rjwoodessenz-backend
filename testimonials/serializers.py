from rest_framework import serializers
from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    customer_photo_url = serializers.SerializerMethodField()
    product_photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = [
            'id',
            'customer_name',
            'customer_photo',
            'customer_photo_url',
            'review',
            'star_rating',
            'product_photo',
            'product_photo_url',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'customer_photo_url', 'product_photo_url']

    def get_customer_photo_url(self, obj):
        if obj.customer_photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.customer_photo.url)
            return obj.customer_photo.url
        return None

    def get_product_photo_url(self, obj):
        if obj.product_photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.product_photo.url)
            return obj.product_photo.url
        return None
