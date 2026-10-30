import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pahilopaila_core.settings')
django.setup()

from school.models import SchoolInfo

info = SchoolInfo.objects.first()
if not info:
    info = SchoolInfo()

info.name = "Pahilo Paila Montessori School"
info.address = "Suda, Mahendranagar, Nepal"
info.phone = "984-8636068"
info.email = "Pahilopaila1@gmail.com"
info.facebook_url = "https://www.facebook.com/p/Pahilo-Paila-Montessori-School-61569129280008/"
info.opening_hours = "Sun - Fri: 8:30 AM - 4:00 PM"
info.motto = "Nurturing Curious Minds, Shaping Joyful Futures (पहिलो पाइला Montessori School)"
info.save()

print("School contact and address details successfully updated in database:")
print(f"Address: {info.address}")
print(f"Phone: {info.phone}")
print(f"Email: {info.email}")
