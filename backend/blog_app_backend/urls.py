from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView, CategoryView, BlogPostCategoryView, \
    RecentPostsView

urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    path('category/', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
    path('categories', CategoryView.as_view()),
    path('categories/<int:pk>', CategoryView.as_view()),
    path('recent/', RecentPostsView.as_view()),
]
