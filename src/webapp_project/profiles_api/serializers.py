from rest_framework import serializers

from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileUploadFileSerializer(serializers.ModelSerializer):
    """A serializer for profile uploaded files."""

    image = serializers.ImageField(max_length=None, use_url=True)
    datafile = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = models.ProfileUploadFile
        fields = ('id', 'user_profile', 'file_desc', 'created_on', 'image', 'datafile')
        extra_kwargs = {'user_profile': {'read_only': True}}
