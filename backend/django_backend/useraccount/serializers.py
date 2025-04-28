# useraccount/serializers.py - Attempt 3
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True, max_length=255)

    def validate(self, attrs):
        # Explicitly remove username from attributes *before* parent validation happens
        attrs.pop('username', None)
        # Call parent validation AFTER removing username
        attrs = super().validate(attrs)
        return attrs

    # We might not need get_cleaned_data override if validate works
    # def get_cleaned_data(self): ...

    def save(self, request):
        # Ensure username is not in validated_data before calling super().save()
        self.validated_data.pop('username', None)
        user = super().save(request)
        user.name = self.validated_data.get('name', '')
        user.save(update_fields=['name'])
        return user

    # NO Meta class defined here