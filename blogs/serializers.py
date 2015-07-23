# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('owner',)


class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ('title', 'imageUrl', 'abstract', "publication_date")

