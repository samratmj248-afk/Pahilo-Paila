import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pahilopaila_core.settings')
django.setup()

from school.models import SchoolInfo, GalleryImage, SchoolEvent

# Update School Info to reference Mahendranagar and official FB page
info = SchoolInfo.objects.first()
if info:
    info.address = "Mahendranagar, Kanchanpur, Nepal"
    info.facebook_url = "https://www.facebook.com/p/Pahilo-Paila-Montessori-School-61569129280008/"
    info.motto = "Nurturing Curious Minds, Shaping Joyful Futures (पहिलो पाइला Montessori School)"
    info.save()
    print("SchoolInfo updated.")

# Update/Add Gallery images matching the real FB page activities (Pencil Picking, Color Hunting, Celebrations)
activities = [
    {
        "title": "Colour Hunting & Sorting Game",
        "category": "sensorial",
        "image_url": "https://images.unsplash.com/photo-1596495578065-6e0763fa1178?auto=format&fit=crop&w=800&q=80",
        "caption": "Children actively identifying and classifying primary & secondary colors in the classroom.",
        "order": 1
    },
    {
        "title": "Pencil Picking Dexterity Race",
        "category": "sensorial",
        "image_url": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?auto=format&fit=crop&w=800&q=80",
        "caption": "Strengthening 3-finger pincer grasp for effortless pre-writing mastery.",
        "order": 2
    },
    {
        "title": "Montessori Birthday Celebration of Life",
        "category": "celebrations",
        "image_url": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=800&q=80",
        "caption": "Walking around the sun to learn the solar cycle and celebrating every child's growth.",
        "order": 3
    },
    {
        "title": "Practical Life: Water Pouring & Spilling Cleanup",
        "category": "classroom",
        "image_url": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=800&q=80",
        "caption": "Fostering early independence, self-reliance, and balance.",
        "order": 4
    }
]

for act in activities:
    GalleryImage.objects.update_or_create(
        title=act["title"],
        defaults=act
    )

print("Updated FB activities and School details.")
