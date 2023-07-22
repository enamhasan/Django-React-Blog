from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView, CategoryView, BlogPostCategoryView, \
    RecentPostsView, ContactView, react_app

from . import views

urlpatterns = [
    path('', views.react_app, name='react_app'),
    path('test', BlogPostListView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    path('category/', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
    path('categories', CategoryView.as_view()),
    path('categories/<int:pk>', CategoryView.as_view()),
    path('recent/', RecentPostsView.as_view()),
    path('contact/', ContactView.as_view()),
]
