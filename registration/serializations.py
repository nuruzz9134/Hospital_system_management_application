from rest_framework import serializers
from registration.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class superuserSerializer(serializers.ModelSerializer):
    # we are writing this because we need confirm password2 field in our Registration Request
    password2 = serializers.CharField(style={'input_type' : 'password'},write_only=True)
    class Meta:
        model= User
        fields = ['name','phone','password','password2']
        extra_kwargs = {'password' : {'write_only':True}    }


    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password does not match")
        return attrs

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)




class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this because we need confirm password2 field in our Registration Request
    password2 = serializers.CharField(style={'input_type' : 'password'},write_only=True)
    class Meta:
        model= User
        fields = ['name','phone','password','password2']
        extra_kwargs = {'password' : {'write_only':True}    }


    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password does not match")
        return attrs

    def create(self, validated_data):
         return User.objects.create_user(**validated_data)




class UserLoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['phone','password']