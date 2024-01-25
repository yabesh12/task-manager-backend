from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Handles the serialization and deserialization of User objects.
    """
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        """
        Validate the password to ensure it meets the minimum length requirement.

        Parameters:
        - value: The password to be validated.

        Returns:
        - str: The validated password.

        Raises:
        - serializers.ValidationError: If the password is too short.
        """
        if len(value) < 5:
            raise serializers.ValidationError("Password must be at least 5 characters long.")
        return value

    def create(self, validated_data):
        """
        Create a new User instance with the provided validated data.

        Parameters:
        - validated_data: Validated data for creating a new User.

        Returns:
        - User: The newly created User instance.
        """
        user = User.objects.create_user(**validated_data)
        return user
