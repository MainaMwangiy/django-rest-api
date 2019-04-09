from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    '''Serializes a name ffield for testing our APIView'''

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    '''A serializer for the user profile object'''

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        '''Create and return a new user.'''

        user = models.UserProfile(
            email=validated_data.get('email'),
            name=validated_data.get('name')
        )
        user.set_password(validated_data.get('password'))
        user.save()

        return user
