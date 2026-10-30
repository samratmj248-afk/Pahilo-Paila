import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pahilopaila_core.settings')
django.setup()

from school.models import SchoolEvent

for e in SchoolEvent.objects.all():
    if "Campus" in e.location or "campus" in e.location:
        e.location = "Pahilo Paila Montessori, Suda, Mahendranagar"
        e.save()

print("Cleaned event locations in database.")
