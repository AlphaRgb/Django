from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Book, Chapter

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BookSerializer

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


def index(request):
    posts = Post.objects.all().order_by('-created_time')
    return render(request, 'blogs/index.html', context={'posts': posts})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogs/detail.html', context={'post': post})


# class BookView(APIView):
# 	def get(self,request,format=None):
# 		books = Book.objects.all()
# 		book_serializer = BookSerializer(books,many=True)
# 		return Response(book_serializer.data)

# class BookListView(mixins.ListModelMixin,generics.GenericAPIView):
# 	queryset = Book.objects.all()
# 	serializer_class = BookSerializer

# 	def get(self,request,*args,**kwargs):
# 		return self.list(request,*args,**kwargs)

from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination


from django_filters.rest_framework import DjangoFilterBackend


class BookListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    throttle_classes = (UserRateThrottle, AnonRateThrottle,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'author')

# def get_queryset(self):
# 	queryset = Book.objects.all()
# 	_id = self.request.query_params.get('id',0)
# 	if _id:
# 		queryset = queryset.filter(id=_id)
# 	return queryset
