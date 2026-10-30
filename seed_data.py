import os
import django
from django.utils import timezone
from datetime import date, time, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pahilopaila_core.settings')
django.setup()

from django.contrib.auth.models import User
from school.models import (
    SchoolInfo, Program, StaffMember, AdmissionInquiry,
    SchoolEvent, GalleryImage, Testimonial, Notice, ContactMessage
)

# 1. Create Superuser for Unfold CMS
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@pahilopaila.edu.np', 'admin123')
    print("Superuser 'admin' created with password 'admin123'")
else:
    print("Superuser 'admin' already exists.")

# 2. Populate School Info
if not SchoolInfo.objects.exists():
    SchoolInfo.objects.create(
        name="Pahilo Paila Montessori",
        motto="Nurturing Curious Minds, Shaping Joyful Futures (पहिलो पाइला Montessori)",
        phone="+977-1-4567890 / +977-9801234567",
        email="hello@pahilopaila.edu.np",
        address="Peaceful Meadows Lane, Kathmandu, Nepal",
        opening_hours="Sun - Fri: 8:30 AM - 4:00 PM",
        about_text="Pahilo Paila Montessori offers a scientific child-centered learning community designed by Dr. Maria Montessori. We cultivate confidence, independence, and holistic intelligence.",
        facebook_url="https://facebook.com",
        instagram_url="https://instagram.com",
        youtube_url="https://youtube.com"
    )
    print("SchoolInfo initialized.")

# 3. Populate Programs
if not Program.objects.exists():
    programs_data = [
        {
            "title": "Infant Community (Nido)",
            "slug": "infant-community",
            "age_group": "infant",
            "timing": "9:00 AM - 12:30 PM",
            "capacity": 10,
            "description": "A tranquil, safe space where babies and young toddlers develop gross motor mastery, object permanence, language emergence, and emotional security with certified infant guides.",
            "highlights": "Gross motor movement area\nSensory treasure baskets\nGentle responsive weaning\nLanguage immersion & lullabies",
            "icon": "bi-heart-pulse",
            "color_accent": "#FF6B6B",
            "order": 1
        },
        {
            "title": "Toddler Explorers Community",
            "slug": "toddler-explorers",
            "age_group": "toddler",
            "timing": "9:00 AM - 1:00 PM",
            "capacity": 15,
            "description": "Fostering practical life independence, joyful toilet learning, vocabulary bursts, and social grace. Toddlers work with specially scaled wooden materials.",
            "highlights": "Practical life self-care\nFood prep & table setting\nFine motor dexterity puzzles\nEmotional coaching & peer sharing",
            "icon": "bi-stars",
            "color_accent": "#4ECDC4",
            "order": 2
        },
        {
            "title": "Primary / Casa dei Bambini",
            "slug": "casa-primary",
            "age_group": "primary",
            "timing": "8:45 AM - 2:30 PM",
            "capacity": 20,
            "description": "Our signature 3-year Montessori cycle. Children manipulate sensorial geometry, phonetic movable alphabets, golden bead arithmetic, botany, and cultural geography.",
            "highlights": "Movable alphabet & phonetics\nGolden beads decimal math\nBotany & cultural geography\nUninterrupted 3-hour work cycle",
            "icon": "bi-book",
            "color_accent": "#FFB74D",
            "order": 3
        },
        {
            "title": "After-School & Creative Discovery",
            "slug": "afterschool-discovery",
            "age_group": "afterschool",
            "timing": "2:30 PM - 5:30 PM",
            "capacity": 25,
            "description": "Enrichment club offering pottery, musical rhythms, nature gardening, mindfulness, and creative storytelling in a warm, relaxed after-school atmosphere.",
            "highlights": "Clay pottery & visual arts\nOrganic kitchen gardening\nYoga & mindfulness for kids\nNepali & World folk storytelling",
            "icon": "bi-palette",
            "color_accent": "#7C4DFF",
            "order": 4
        }
    ]
    for p in programs_data:
        Program.objects.create(**p)
    print("Programs initialized.")

# 4. Populate Staff Members
if not StaffMember.objects.exists():
    staff_data = [
        {
            "name": "Prerana Adhikari, M.Ed",
            "role": "principal",
            "qualifications": "AMI Diploma (Amsterdam), M.Ed Early Childhood Development",
            "experience_years": 14,
            "bio": "Dedicated educator with 14+ years pioneering authentic Montessori education across South Asia. Passionate about natural curiosity and mindful parenting.",
            "avatar_url": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=600&q=80",
            "order": 1
        },
        {
            "name": "Sushant Thapa",
            "role": "lead_guide",
            "qualifications": "AMI Primary Certified (Casa Lead Guide)",
            "experience_years": 8,
            "bio": "Specializes in sensorial arithmetic and language immersion. Sushant guides children in developing deep concentration and love for exploration.",
            "avatar_url": "https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=600&q=80",
            "order": 2
        },
        {
            "name": "Ananya Karki",
            "role": "pediatric_care",
            "qualifications": "Child Nutritionist & Infant Care Specialist",
            "experience_years": 6,
            "bio": "Oversees balanced wholesome meals, organic hygiene protocols, and child wellness standards at Pahilo Paila.",
            "avatar_url": "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=600&q=80",
            "order": 3
        },
        {
            "name": "Binod Maharjan",
            "role": "arts",
            "qualifications": "M.F.A. Fine Arts & Traditional Music Educator",
            "experience_years": 7,
            "bio": "Inspires creative tactile expressions, rhythm games, clay sculpting, and expressive dance for young learners.",
            "avatar_url": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80",
            "order": 4
        }
    ]
    for s in staff_data:
        StaffMember.objects.create(**s)
    print("Staff members initialized.")

# 5. Populate Testimonials
if not Testimonial.objects.exists():
    testimonials_data = [
        {
            "parent_name": "Roshani & Bikash Shrestha",
            "child_name_and_grade": "Parents of Aarav (Casa Level 2)",
            "rating": 5,
            "content": "Pahilo Paila transformed our son's focus and confidence. At 4 years old, he sets his own breakfast plate, cleans his spills, and reads whole phonics books with sheer joy!",
            "avatar_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=300&q=80"
        },
        {
            "parent_name": "Dr. Nirajan Pandey",
            "child_name_and_grade": "Parent of Anvi (Toddler Community)",
            "rating": 5,
            "content": "The calm, orderly, yet stimulating environment is something you rarely find in Kathmandu. The guides treat every child with immense respect and care.",
            "avatar_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=300&q=80"
        },
        {
            "parent_name": "Pooja Gurung",
            "child_name_and_grade": "Parent of Kabir (Casa Level 1)",
            "rating": 5,
            "content": "The campus security, organic meals, and personalized updates give us complete peace of mind. We couldn't imagine a better first step (पहिलो पाइला) for our son!",
            "avatar_url": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80"
        }
    ]
    for t in testimonials_data:
        Testimonial.objects.create(**t)
    print("Testimonials initialized.")

# 6. Populate Gallery Images
if not GalleryImage.objects.exists():
    gallery_data = [
        {"title": "Practical Life: Flower Arranging", "category": "sensorial", "image_url": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?auto=format&fit=crop&w=800&q=80", "caption": "Developing concentration and fine motor control.", "order": 1},
        {"title": "Montessori Pink Tower Exploration", "category": "classroom", "image_url": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=800&q=80", "caption": "Visual discrimination of three dimensions.", "order": 2},
        {"title": "Sensory Nature Garden", "category": "nature", "image_url": "https://images.unsplash.com/photo-1596495578065-6e0763fa1178?auto=format&fit=crop&w=800&q=80", "caption": "Planting organic herbs and observing caterpillars.", "order": 3},
        {"title": "Creative Clay & Color Studio", "category": "creativity", "image_url": "https://images.unsplash.com/photo-1560421683-680b9c814e52?auto=format&fit=crop&w=800&q=80", "caption": "Free-form tactile pottery and finger painting.", "order": 4},
        {"title": "Celebration of Cultural Harmony", "category": "celebrations", "image_url": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=800&q=80", "caption": "Learning global traditions and empathy.", "order": 5},
        {"title": "Child-sized Culinary Prep Area", "category": "sensorial", "image_url": "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=800&q=80", "caption": "Slicing soft bananas and pouring water independently.", "order": 6}
    ]
    for g in gallery_data:
        GalleryImage.objects.create(**g)
    print("Gallery images initialized.")

# 7. Populate Events & Notices
if not SchoolEvent.objects.exists():
    SchoolEvent.objects.create(
        title="Spring Montessori Open House & Discovery Day",
        event_date=date.today() + timedelta(days=7),
        start_time=time(10, 0),
        end_time=time(14, 0),
        location="Pahilo Paila Central Campus Ground",
        description="Experience live Montessori classroom demonstrations, meet lead guides, and let your child explore tactile materials.",
        is_public=True
    )
    SchoolEvent.objects.create(
        title="Positive Parenting Workshop: Dr. Montessori at Home",
        event_date=date.today() + timedelta(days=21),
        start_time=time(11, 0),
        end_time=time(13, 0),
        location="Pahilo Paila Seminar Auditorium",
        description="Learn practical strategies to structure your home environment for independence and stress-free routines.",
        is_public=True
    )
    print("Events initialized.")

if not Notice.objects.exists():
    Notice.objects.create(
        title="Spring Admissions Open for Infant, Toddler & Casa Cohorts",
        urgency="important",
        content="Applications for the upcoming Spring academic term are now open. Limited seats per cohort to preserve authentic student-guide ratio.",
        publish_date=date.today(),
        is_active=True
    )
    print("Notices initialized.")

print("All sample data seeded successfully!")
