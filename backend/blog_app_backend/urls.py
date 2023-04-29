from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>/', CategoryView.as_view()),
]
