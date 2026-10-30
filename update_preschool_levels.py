import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pahilopaila_core.settings')
django.setup()

from school.models import Program, SchoolInfo

info = SchoolInfo.objects.first()
if info:
    info.about_text = "Pahilo Paila Montessori School in Suda, Mahendranagar provides authentic, child-centered early childhood education. We nurture curiosity, motor coordination, cognitive growth, and self-directed learning in a loving preschool environment."
    info.save()

# Reseed preschool level programs
Program.objects.all().delete()

programs_data = [
    {
        "title": "Playgroup / Toddler Community",
        "slug": "playgroup-toddler",
        "age_group": "playgroup",
        "timing": "9:30 AM - 1:00 PM",
        "capacity": 15,
        "description": "A gentle, nurturing introduction to school life. Toddlers build motor dexterity, speech, social sharing, and joyful self-reliance through sensory toys and games.",
        "highlights": "Sensory discovery baskets\nPencil picking & grip exercises\nColour identification & sorting\nMusic, rhymes & story circles",
        "icon": "bi-balloon-heart",
        "color_accent": "#FF6B6B",
        "order": 1
    },
    {
        "title": "Nursery Montessori Program",
        "slug": "nursery-program",
        "age_group": "nursery",
        "timing": "9:30 AM - 1:30 PM",
        "capacity": 18,
        "description": "Cultivating practical life independence, phonics sounds, hand-eye coordination, and spatial reasoning through Dr. Montessori's classic sensorial materials.",
        "highlights": "Practical life water & pouring exercises\nPhonics sound cards & picture matching\nPink tower dimension stacking\nCreative finger art & clay sculpting",
        "icon": "bi-stars",
        "color_accent": "#4ECDC4",
        "order": 2
    },
    {
        "title": "LKG / Casa Junior",
        "slug": "lkg-casa-junior",
        "age_group": "lkg",
        "timing": "9:00 AM - 2:00 PM",
        "capacity": 20,
        "description": "Children actively explore number quantities, tactile sandpaper letters, conversational Nepali & English, nature exploration, and collaborative teamwork.",
        "highlights": "Sandpaper letters & word building\nNumber rods & counting beads\nOutdoor nature games & races\nInteractive conversational immersion",
        "icon": "bi-book",
        "color_accent": "#FFB74D",
        "order": 3
    },
    {
        "title": "UKG / Casa Senior",
        "slug": "ukg-casa-senior",
        "age_group": "ukg",
        "timing": "9:00 AM - 2:30 PM",
        "capacity": 20,
        "description": "Preparing young minds for primary school with strong reading fluency, mathematical decimal bead concepts, creative drawing, and leadership confidence.",
        "highlights": "Fluent early reading & sentence crafting\nAddition & subtraction concrete beads\nMontessori Celebration of Life traditions\nSelf-directed project work cycles",
        "icon": "bi-award",
        "color_accent": "#7C4DFF",
        "order": 4
    }
]

for p in programs_data:
    Program.objects.create(**p)

print("Preschool & Montessori levels updated successfully.")
