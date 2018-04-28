from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)
    print(post)
    return render(request, 'blog/post/detail.html')

from rest_framework.views import APIView,status
from rest_framework.response import Response
from .serializers import PostSerializer

# class PostListView(APIView):
#     def get(self,request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

from rest_framework import mixins
from rest_framework import generics

# class PostListView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

from rest_framework import viewsets

class PostListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    search_fields = ('title','body')
    ordering_fields = ('publish',)

    # def get_queryset(self):
    #     return Post.objects.filter()



    