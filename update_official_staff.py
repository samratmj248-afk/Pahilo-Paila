import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pahilopaila_core.settings')
django.setup()

from school.models import StaffMember

# Delete old placeholder staff
StaffMember.objects.all().delete()

staff_list = [
    {
        'name': 'Avhilasha Singh',
        'role': 'principal',
        'qualifications': 'Principal & Senior Montessori Administrator',
        'experience_years': 8,
        'bio': 'Guiding Pahilo Paila Montessori with passionate leadership, dedicated to holistic child development, nurturing environment, and authentic Montessori philosophy.',
        'avatar_url': '/static/img/staff/avhilasha_singh_principal.webp',
        'order': 1
    },
    {
        'name': 'Pooja Joshi',
        'role': 'lead_guide',
        'qualifications': 'Certified Lead Montessori Guide (Toddler & Casa)',
        'experience_years': 6,
        'bio': 'Specialized in sensorial apparatus guidance and speech-motor coordination for early foundation cohorts.',
        'avatar_url': '/static/img/staff/staff_1.webp',
        'order': 2
    },
    {
        'name': 'Sita Bhandari',
        'role': 'teacher',
        'qualifications': 'Early Childhood Care & Montessori Teacher',
        'experience_years': 5,
        'bio': 'Facilitating practical life exercises, independence routines, and playful language immersion for young learners.',
        'avatar_url': '/static/img/staff/staff_3.webp',
        'order': 3
    },
    {
        'name': 'Gita Chand',
        'role': 'teacher',
        'qualifications': 'Montessori Primary Level Educator',
        'experience_years': 4,
        'bio': 'Passionate about mathematical bead manipulation, nature discovery, and cooperative peer play.',
        'avatar_url': '/static/img/staff/staff_4.webp',
        'order': 4
    },
    {
        'name': 'Radha Rana',
        'role': 'teacher',
        'qualifications': 'Montessori Child Development Specialist',
        'experience_years': 5,
        'bio': 'Nurturing motor coordination, storytelling circles, and sensorial color-sorting activities.',
        'avatar_url': '/static/img/staff/staff_5.webp',
        'order': 5
    },
    {
        'name': 'Laxmi Pant',
        'role': 'teacher',
        'qualifications': 'Montessori Teacher & Creative Learning Guide',
        'experience_years': 4,
        'bio': 'Encouraging hands-on tactile discovery, drawing, and positive emotional bonding among preschool cohorts.',
        'avatar_url': '/static/img/staff/staff_6.webp',
        'order': 6
    },
    {
        'name': 'Manisha Rawal',
        'role': 'arts',
        'qualifications': 'Creative Expression & Movement Educator',
        'experience_years': 3,
        'bio': 'Inspiring young imaginations through musical rhymes, finger painting, and joyful cultural celebrations.',
        'avatar_url': '/static/img/staff/staff_7.webp',
        'order': 7
    },
    {
        'name': 'Kamala Saud',
        'role': 'care',
        'qualifications': 'Child Caregiver & Nutrition Assistant',
        'experience_years': 5,
        'bio': 'Ensuring loving comfort, daily hygienic routines, and wholesome organic snack support throughout school hours.',
        'avatar_url': '/static/img/staff/staff_8.webp',
        'order': 8
    },
]

for s in staff_list:
    obj = StaffMember.objects.create(**s)
    print(f"Created: {obj.order}. {obj.name} ({obj.get_role_display()})")

print(f"Total staff members: {StaffMember.objects.count()}")
