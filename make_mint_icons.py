import os
from PIL import Image, ImageDraw

os.makedirs('static/img', exist_ok=True)

img = Image.new('RGBA', (512, 512), color=(15, 23, 42, 255))
draw = ImageDraw.Draw(img)

# Outer circle ring
draw.ellipse([20, 20, 492, 492], fill=(22, 33, 56, 255), outline=(78, 205, 196, 255), width=10)

# Draw white embossed ribbon & mint center
# Big Toe
draw.ellipse([340, 110, 410, 190], fill=(255, 255, 255, 255))
draw.ellipse([352, 122, 398, 178], fill=(78, 205, 196, 255))

# Toe 2
draw.ellipse([275, 75, 335, 145], fill=(255, 255, 255, 255))
draw.ellipse([285, 85, 325, 135], fill=(78, 205, 196, 255))

# Toe 3
draw.ellipse([210, 65, 265, 130], fill=(255, 255, 255, 255))
draw.ellipse([220, 75, 255, 120], fill=(78, 205, 196, 255))

# Toe 4
draw.ellipse([150, 85, 200, 145], fill=(255, 255, 255, 255))
draw.ellipse([158, 93, 192, 137], fill=(78, 205, 196, 255))

# Toe 5
draw.ellipse([95, 130, 140, 180], fill=(255, 255, 255, 255))
draw.ellipse([102, 138, 133, 172], fill=(78, 205, 196, 255))

# Swirling Foot Sole Path
draw.polygon([(160, 200), (360, 190), (320, 310), (220, 360), (280, 440), (220, 460), (170, 380), (120, 260)], fill=(255, 255, 255, 255))
draw.polygon([(180, 215), (335, 210), (295, 305), (205, 355), (260, 425), (230, 440), (190, 375), (145, 270)], fill=(78, 205, 196, 255))

img.save('static/img/icon-512.png')
img_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
img_192.save('static/img/icon-192.png')

print("Icons generated for mint footprint logo.")
