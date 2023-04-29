from django.test import TestCase
from .models import Category, Post

# Create your tests here.

def test_Categorymodel(self):
    category = Category.objects.create(name='test category')
    self.assertEqual(category.name, 'test category')
    self.assertEqual(category.slug, 'test-category')

def test_Postmodel(self):
    category = Category.objects.create(name='test category')
    post = Post.objects.create(title='test post', content='test content', category=category)
    self.assertEqual(post.title, 'test post')
    self.assertEqual(post.slug, 'test-post')
    self.assertEqual(post.content, 'test content')
    self.assertEqual(post.category, category)

def test_CategoryView(self):
    category = Category.objects.create(name='test category')
    response = self.client.get('/api/category/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data[0]['name'], 'test category')
    self.assertEqual(response.data[0]['slug'], 'test-category')




