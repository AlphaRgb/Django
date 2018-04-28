#!/usr/bin/env python3
# coding=utf-8

from django.views.generic.base import View
from .models import Post
import json

class PostListView(View):
    def get(self,request):
        json_list = []
        posts = Post.objects.all()
        # for post in posts:
        #     d = {}
        #     d['title'] = post.title
        #     d['body'] = post.body
        #     d['publish'] = post.publish
        #     json_list.append(d)
        from django.forms.models import model_to_dict
        for post in posts:
            d = model_to_dict(post)
            json_list.append(d)
        from django.core import serializers
        json_data = serializers.serialize('json',posts)
        json_data = json.loads(json_data)
        from django.http import HttpResponse,JsonResponse
        return JsonResponse(json_data)


