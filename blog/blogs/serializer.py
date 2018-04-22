#!/usr/bin/env python3
# coding:utf-8

from rest_framework import serializers
from .models import Book,Category

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # def create(self,validated_data):
    # 	return Book.objects.create(**validated_data)
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = "__all__"
