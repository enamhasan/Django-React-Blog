import pytest
from .models import Category, Post

@pytest.mark.django_db
def test_category():
    category = Category.objects.create(name='python')
    assert category.name == 'python'
