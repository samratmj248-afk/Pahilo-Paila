from .models import SchoolInfo, Notice

def school_context(request):
    school_info = SchoolInfo.objects.first()
    active_notices = Notice.objects.filter(is_active=True)[:3]
    return {
        'school_info': school_info,
        'active_notices': active_notices,
    }
