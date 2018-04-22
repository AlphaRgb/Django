#!/usr/bin/env python3
# coding:utf-8

from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


## 1
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(required=True,max_length=100)
#     slug = serializers.CharField()
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)


## 2
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Post
        # fields = ('title','slug','author','body')
        fields = '__all__'

