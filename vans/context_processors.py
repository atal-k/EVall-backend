# ============================================================================
# FILE: vans/context_processors.py
# NEW FILE: Context processor for dashboard stats
# ============================================================================

from vans.models import Van

def admin_stats(request):
    '''Provide van statistics to admin templates'''
    if request.path.startswith('/admin'):
        return {
            'light_duty_count': Van.objects.filter(category='light-duty').count(),
            'medium_duty_count': Van.objects.filter(category='medium-duty').count(),
            'heavy_duty_count': Van.objects.filter(category='heavy-duty').count(),
            'featured_count': Van.objects.filter(is_featured=True).count(),
        }
    return {}