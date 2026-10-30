import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('static/img', exist_ok=True)

# Create 512x512 app icon matching official logo
img = Image.new('RGBA', (512, 512), color=(255, 255, 255, 255))
draw = ImageDraw.Draw(img)

# Outer rounded border / shield
draw.rounded_rectangle([16, 16, 496, 496], radius=64, fill=(255, 255, 255, 255), outline=(14, 47, 108, 255), width=8)

# Draw Emerald Green footprint
# Big toe
draw.ellipse([340, 110, 390, 170], fill=(0, 176, 116, 255))
# Small toes
draw.ellipse([275, 95, 315, 140], fill=(0, 176, 116, 255))
draw.ellipse([220, 110, 255, 150], fill=(0, 176, 116, 255))
draw.ellipse([175, 140, 205, 175], fill=(0, 176, 116, 255))
draw.ellipse([140, 180, 165, 210], fill=(0, 176, 116, 255))

# Sole & Heel
draw.polygon([(260, 180), (380, 190), (330, 350), (220, 350)], fill=(0, 176, 116, 255))
draw.ellipse([210, 300, 330, 410], fill=(0, 176, 116, 255))

img.save('static/img/icon-512.png')
img_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
img_192.save('static/img/icon-192.png')

print("PWA icons updated to match official green footprint logo.")
