from django.contrib.auth import get_user_model
from django.db import transaction
from apps.tenants.models import Tenant

User = get_user_model()


class AccountService:

    @staticmethod
    @transaction.atomic
    def register_tenant_with_admin(validated_data: dict):
        tenant = Tenant.objects.create(
            name=validated_data['company_name']
        )

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            tenant=tenant,
        )

        return tenant, user
