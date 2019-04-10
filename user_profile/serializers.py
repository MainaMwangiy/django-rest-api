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


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''A serializer for the profile feed.'''

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

    def create(self, validated_data):
        '''Create and return a new profile feed.'''

        profile_feed_item = models.ProfileFeedItem(
            user_profile=validated_data.get('user_profile'),
            status_text=validated_data.get('status_text'),
            created_on=validated_data.get('created_on')
        )

        profile_feed_item.save()

        return profile_feed_item
