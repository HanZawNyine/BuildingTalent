from rest_framework import serializers

from social.models import Post


class SocialPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'body', 'publish', 'created']
