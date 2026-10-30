import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('static/img', exist_ok=True)

# Generate 512x512
img = Image.new('RGBA', (512, 512), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw rounded circle / shield gradient background
draw.ellipse([16, 16, 496, 496], fill=(255, 94, 98, 255), outline=(255, 153, 102, 255), width=12)
# Inner circle
draw.ellipse([64, 64, 448, 448], fill=(16, 24, 48, 255))

# Draw footprint / stepping stones art & star
# Big toe
draw.ellipse([216, 140, 296, 260], fill=(255, 183, 77, 255))
# Small toes
draw.ellipse([160, 150, 195, 185], fill=(255, 107, 107, 255))
draw.ellipse([190, 110, 230, 150], fill=(78, 205, 196, 255))
draw.ellipse([280, 110, 320, 150], fill=(168, 230, 207, 255))
draw.ellipse([320, 150, 355, 185], fill=(255, 217, 61, 255))
# Foot ball & heel
draw.polygon([(200, 240), (312, 240), (280, 370), (232, 370)], fill=(255, 183, 77, 255))
draw.ellipse([210, 340, 302, 420], fill=(255, 183, 77, 255))

img.save('static/img/icon-512.png')

# Generate 192x192
img_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
img_192.save('static/img/icon-192.png')

# Generate SVG Logo
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 100" fill="none">
  <circle cx="50" cy="50" r="42" fill="url(#grad)" />
  <circle cx="50" cy="50" r="34" fill="#0f172a" />
  <path d="M42 38 C42 32, 58 32, 58 38 C58 48, 42 54, 50 68" stroke="#ffb74d" stroke-width="4" stroke-linecap="round"/>
  <circle cx="50" cy="74" r="3.5" fill="#ff6b6b" />
  <circle cx="34" cy="38" r="3" fill="#4ecdc4" />
  <circle cx="66" cy="38" r="3" fill="#a8e6cf" />
  <text x="105" y="48" font-family="'Outfit', sans-serif" font-weight="800" font-size="28" fill="#ffffff">PAHILO <tspan fill="#ff6b6b">PAILA</tspan></text>
  <text x="106" y="72" font-family="'Plus Jakarta Sans', sans-serif" font-weight="600" font-size="12" fill="#94a3b8" letter-spacing="2">MONTESSORI SCHOOL</text>
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff5e62" />
      <stop offset="100%" stop-color="#ff9966" />
    </linearGradient>
  </defs>
</svg>'''

with open('static/img/logo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("Icons & SVG logo generated successfully.")
