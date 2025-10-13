# ============================================================================
# FILE: vans/forms.py
# NEW FILE: Custom admin form with Cloudinary widget
# ============================================================================

from django import forms
from django.conf import settings
from .models import Van

class CloudinaryImagesWidget(forms.Widget):
    """Custom widget for Cloudinary multi-image upload"""
    
    template_name = 'admin/widgets/cloudinary_images.html'
    
    class Media:
        js = (
            'https://upload-widget.cloudinary.com/global/all.js',
            'vans/js/cloudinary_admin_uploader.js',
        )
        css = {
            'all': ('vans/css/cloudinary_admin.css',)
        }
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['cloud_name'] = settings.CLOUDINARY.get('cloud_name', '')
        context['widget']['upload_preset'] = 'evall_vans_unsigned'
        context['widget']['current_images'] = value if value else []
        return context


class VanAdminForm(forms.ModelForm):
    """Custom form for Van admin with Cloudinary uploader"""
    
    images = forms.JSONField(
        widget=CloudinaryImagesWidget(),
        required=False,
        help_text="Upload van images using Cloudinary"
    )
    
    class Meta:
        model = Van
        fields = '__all__'