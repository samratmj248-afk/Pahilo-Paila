import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pahilopaila_core.settings')
django.setup()

from school.models import GalleryImage

items = [
    {
        'title': 'Welcome to Our School (Pahilo Paila)',
        'category': 'celebrations',
        'image_url': '/static/img/gallery/welcome_school_gathering.webp',
        'caption': 'Our little champions smiling together during the welcome ceremony at Pahilo Paila Montessori, Suda.',
        'order': 1
    },
    {
        'title': 'National Paddy Day Outdoor Activity',
        'category': 'nature',
        'image_url': '/static/img/gallery/dhan_diwas_rice_plantation.webp',
        'caption': 'Hands-on practical life learning: toddlers experiencing traditional rice paddy transplantation with natural soil and water.',
        'order': 2
    },
    {
        'title': 'Rastriya Dhan Diwas Ceremony',
        'category': 'celebrations',
        'image_url': '/static/img/gallery/dhan_diwas_celebration.webp',
        'caption': 'Children proudly wearing Nepali cultural and school attire celebrating traditional agriculture and harvesting joy.',
        'order': 3
    },
    {
        'title': 'Holi Festival Sensory Color Play',
        'category': 'sensorial',
        'image_url': '/static/img/gallery/holi_colors_activity.webp',
        'caption': 'Sensory and social harmony: toddlers celebrating colors and friendship in a safe, organic classroom environment.',
        'order': 4
    },
    {
        'title': 'Students & Educators Assembly',
        'category': 'classroom',
        'image_url': '/static/img/gallery/campus_teachers_and_students.webp',
        'caption': 'Our dedicated Montessori guides, caregivers, and happy children under the spacious shaded courtyard.',
        'order': 5
    },
]

for data in items:
    obj, created = GalleryImage.objects.update_or_create(
        title=data['title'],
        defaults=data
    )
    print(f"Saved: {obj.id} - {obj.title}")

print(f"Total Gallery Images: {GalleryImage.objects.count()}")
