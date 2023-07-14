# admincustom/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

# admin site customizations
admin.site.site_header = 'Django React Blog'
admin.site.index_title = 'Blog App'

# URLs
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin', admin.site.urls),
    path('blog/', include('blog_app_backend.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]


