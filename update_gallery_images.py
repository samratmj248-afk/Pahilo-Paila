import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pahilopaila_core.settings')
django.setup()

from school.models import GalleryImage

# Clean and seed gallery images with local static paths and reliable CDNs
GalleryImage.objects.all().delete()

images = [
    {
        "title": "Creative Clay & Color Studio",
        "category": "creativity",
        "image_url": "/static/img/clay_art.jpg",
        "caption": "Joyful tactile finger painting and sensory clay shaping.",
        "order": 1
    },
    {
        "title": "Pencil Picking Dexterity Race",
        "category": "sensorial",
        "image_url": "/static/img/pencil_race.jpg",
        "caption": "Developing pincer grasp and motor agility with wooden color pencils.",
        "order": 2
    },
    {
        "title": "Colour Hunting & Sorting Activity",
        "category": "classroom",
        "image_url": "/static/img/color_hunt.jpg",
        "caption": "Hands-on primary and secondary color classification games.",
        "order": 3
    },
    {
        "title": "Montessori Birthday Celebration of Life",
        "category": "celebrations",
        "image_url": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=800&q=80",
        "caption": "Children walking around the sun celebrating their growth and milestones.",
        "order": 4
    },
    {
        "title": "Practical Life Water Pouring Exercises",
        "category": "sensorial",
        "image_url": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?auto=format&fit=crop&w=800&q=80",
        "caption": "Building early concentration, coordination, and independence.",
        "order": 5
    },
    {
        "title": "Outdoor Nature Exploration & Garden",
        "category": "nature",
        "image_url": "https://images.unsplash.com/photo-1596495578065-6e0763fa1178?auto=format&fit=crop&w=800&q=80",
        "caption": "Exploring sensory plants, textures, and nature observation in Suda.",
        "order": 6
    }
]

for img_data in images:
    GalleryImage.objects.create(**img_data)

print("Gallery database updated with local static assets and reliable images.")
