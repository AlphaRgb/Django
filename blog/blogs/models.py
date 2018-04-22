#!/usr/bin/env python3
# coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('blogs:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    status = models.CharField(max_length=255)
    count_num = models.CharField(max_length=255)
    address_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    num = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    book = models.ForeignKey(Book)

    def __str__(self):
        return self.content







