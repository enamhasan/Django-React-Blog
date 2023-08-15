# admincustom/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from blog_app_backend.views import index

# admin site customizations
admin.site.site_header = 'Django React Blog'
admin.site.index_title = 'Blog App'

# URLs
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('api/', include('blog_app_backend.urls')),
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]


