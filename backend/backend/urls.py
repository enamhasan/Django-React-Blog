#admincustom/urls.py
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = 'Django React Blog'
admin.site.index_title = 'Blog App'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog_app_backend.urls')),

]





