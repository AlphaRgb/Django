from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

# class Post(models.Modle):
# 	STATUS_CHOICES = (
#            ('draft', 'Draft'),
#            ('published', 'Published'),
#        )
# 	title = models.CharField(max_length=250)
# 	slug = models.SlugField(max_length=250,unique_for_date='publish')

# 	author = models.ForeignKey(User,related_name='blog_posts')

# 	body = models.TextField()
# 	publish = models.DateTimeField(default=timezone.now)
# 	created = models.DateTimeField(auto_now_add=True)
# 	updated = models.DateTimeField(auto_now=True)
# 	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

# 	class Meta:
# 		ordering = ('-publish',)

# 	def __str__(self):
# 		return self.title

class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return self.name
