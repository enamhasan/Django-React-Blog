from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Category, Post
from .serializers import CategorySerializer
from rest_framework import status


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
