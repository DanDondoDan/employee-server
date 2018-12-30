import logging

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from employee_server import models

logger = logging.getLogger(__name__)


class PasswordValidator:
    def __call__(self, value):
        if not value:
            return

        error = validate_password(value)
        if error:
            message = error
            raise serializers.ValidationError(message)


class UserPublicSerializer(serializers.ModelSerializer):
    mode = serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = ('email', 'phone', 'birth', )


class UserPrivateSerializer(UserPublicSerializer):
    token = serializers.ReadOnlyField(source='auth_token.key')

    class Meta:
        model = models.User
        fields = UserPublicSerializer.Meta.fields + ('token',)


class UserCreateSerializer(UserPublicSerializer):
    password = serializers.CharField(validators=[PasswordValidator()], allow_blank=True)
    phone = serializers.CharField(allow_blank=True, required=False)
    birth = serializers.DateField(required=True)

    class Meta:
        model = models.User
        write_only_fields = 'password'
        fields = UserPublicSerializer.Meta.fields + ('password', )
        extra_kwargs = {
            'password': {'write_only': True},
            'phone': {'required': False},
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        return user


class ResetPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[PasswordValidator()])

    class Meta:
        model = models.User
        fields = ('password',)
