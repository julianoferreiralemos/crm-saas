from django.contrib.auth import get_user_model
from rest_framework import serializers
from apps.tenants.models import Tenant

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=150, required=False, default='')
    last_name = serializers.CharField(max_length=150, required=False, default='')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este e-mail já está em uso.')
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Este username já está em uso.')
        return value

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({
                'password_confirm': 'As senhas não coincidem.'
            })
        return data


class UserSerializer(serializers.ModelSerializer):
    tenant_name = serializers.CharField(source='tenant.name', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'tenant_name']
        read_only_fields = fields
