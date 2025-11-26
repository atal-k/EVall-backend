from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('enquiries.urls')),
    path('api/', include('blogs.urls')),  # Add this
    path('editorjs/', include('django_editorjs_fields.urls')),  # Add this
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # Serve media files in development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)