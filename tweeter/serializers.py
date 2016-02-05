from django.contrib.auth.models import User

from rest_framework import serializers

from tweeter.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
	creator = serializers.SlugRelatedField(read_only=True, slug_field='username')
	class Meta:
		model = Tweet
		fields = ('text', 'creator', 'timestamp')

class UserSerializer(serializers.ModelSerializer):
	tweets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='text')
	class Meta:
		model = User
		fields = ('id', 'username', 'tweets')