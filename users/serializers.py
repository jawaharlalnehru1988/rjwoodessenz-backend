from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    full_address = serializers.CharField(source='get_full_address', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'user_type', 'phone', 'delivery_address_line1', 'delivery_address_line2',
                 'city', 'state', 'postal_code', 'country', 'share_location', 'full_address', 
                 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'user']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
        read_only_fields = ['id']


class UserRegistrationSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=[('product_buyer', 'Product Buying User'), 
                                                  ('inquiry_maker', 'Inquiry Making User')])
    phone = serializers.CharField(required=True, max_length=15)
    
    # Address fields - required only for product_buyer
    delivery_address_line1 = serializers.CharField(required=False, allow_blank=True)
    delivery_address_line2 = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(required=False, allow_blank=True)
    state = serializers.CharField(required=False, allow_blank=True)
    postal_code = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False, default='India')
    share_location = serializers.URLField(required=False, allow_blank=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 
                 'user_type', 'phone', 'delivery_address_line1', 'delivery_address_line2',
                 'city', 'state', 'postal_code', 'country', 'share_location']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    
    def validate(self, data):
        # If user_type is product_buyer, delivery address is required
        if data.get('user_type') == 'product_buyer':
            required_fields = ['delivery_address_line1', 'city', 'state', 'postal_code']
            for field in required_fields:
                if not data.get(field):
                    raise serializers.ValidationError({
                        field: f"This field is required for Product Buying Users"
                    })
        return data
    
    def create(self, validated_data):
        # Extract profile fields
        user_type = validated_data.pop('user_type')
        phone = validated_data.pop('phone')
        delivery_address_line1 = validated_data.pop('delivery_address_line1', '')
        delivery_address_line2 = validated_data.pop('delivery_address_line2', '')
        city = validated_data.pop('city', '')
        state = validated_data.pop('state', '')
        postal_code = validated_data.pop('postal_code', '')
        country = validated_data.pop('country', 'India')
        share_location = validated_data.pop('share_location', '')
        
        # Create user
        user = User.objects.create_user(**validated_data)
        
        # Create profile
        UserProfile.objects.create(
            user=user,
            user_type=user_type,
            phone=phone,
            delivery_address_line1=delivery_address_line1,
            delivery_address_line2=delivery_address_line2,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            share_location=share_location or None
        )
        
        return user


class UserBasicRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    phone_number = serializers.CharField(required=False, allow_blank=True, max_length=15)
    phoneNumber = serializers.CharField(required=False, allow_blank=True, max_length=15, write_only=True)

    def validate(self, data):
        email = (data.get('email') or '').strip()
        phone_number = (data.get('phone_number') or data.get('phoneNumber') or '').strip()

        if not email and not phone_number:
            raise serializers.ValidationError(
                "Either email or phone number is required."
            )

        if User.objects.filter(username__iexact=data['username']).exists():
            raise serializers.ValidationError({"username": "Username already exists."})

        if email and User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError({"email": "Email already exists."})

        if phone_number and UserProfile.objects.filter(phone=phone_number).exists():
            raise serializers.ValidationError({"phone_number": "Phone number already exists."})

        data['email'] = email
        data['phone_number'] = phone_number
        return data

    def create(self, validated_data):
        email = validated_data.get('email', '')
        phone_number = validated_data.get('phone_number', '')

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=email,
        )

        UserProfile.objects.create(
            user=user,
            user_type='inquiry_maker',
            phone=phone_number or None,
        )

        return user


class UserLoginSerializer(serializers.Serializer):
    phone_or_email = serializers.CharField()
    password = serializers.CharField(write_only=True)
