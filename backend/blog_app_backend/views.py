from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from rest_framework import status


class BlogPostListView(ListAPIView):
    queryset = Post.objects.order_by('-published_on')
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)


class BlogPostDetailView(RetrieveAPIView):
    queryset = Post.objects.order_by('-published_on')
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)


class BlogPostFeaturedView(ListAPIView):
    queryset = Post.objects.all().filter(featured=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)


class BlogPostCategoryView(APIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        print(category)
        queryset = Post.objects.order_by('-published_on').filter(category=category)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class RecentPostsView(ListAPIView):
    queryset = Post.objects.all().order_by('-published_on')[:3]
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)


class CategoryView(APIView):

    def get_categories(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            return category
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            categories = self.get_categories(pk)
            serializer = CategorySerializer(categories)
            return Response(serializer.data)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        category = self.get_categories(pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_categories(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
