import base64

with open(r'c:\Users\maste\OneDrive\Desktop\Pahilo Paila\static\img\official_emblem.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" fill="none">
  <defs>
    <!-- Dynamic Soft Glow -->
    <filter id="logoGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#00A896" flood-opacity="0.35"/>
    </filter>
    
    <!-- Outer Dual-Tone Ring Gradient -->
    <linearGradient id="haloRing" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4ECDC4"/>
      <stop offset="40%" stop-color="#00A896"/>
      <stop offset="80%" stop-color="#FFB74D"/>
      <stop offset="100%" stop-color="#ECA23B"/>
    </linearGradient>

    <!-- Center Disc Radial Gradient -->
    <radialGradient id="discGrad" cx="50%" cy="45%" r="55%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="85%" stop-color="#F0FDFA"/>
      <stop offset="100%" stop-color="#CCFBF1"/>
    </radialGradient>
  </defs>

  <g filter="url(#logoGlow)">
    <!-- Outer Glowing Multi-color Halo Ring -->
    <circle cx="250" cy="250" r="232" stroke="url(#haloRing)" stroke-width="16" fill="none" opacity="0.95"/>
    
    <!-- Inner Delicate Orbit Accent Ring -->
    <circle cx="250" cy="250" r="214" stroke="#00A896" stroke-width="2" stroke-dasharray="6 8" opacity="0.45" fill="none"/>

    <!-- Ambient Orbital Beads -->
    <circle cx="250" cy="18" r="10" fill="#00A896"/>
    <circle cx="250" cy="482" r="10" fill="#ECA23B"/>
    <circle cx="18" cy="250" r="8" fill="#4ECDC4"/>
    <circle cx="482" cy="250" r="8" fill="#F59E0B"/>

    <!-- Inner Clean High-Contrast White/Teal Disc -->
    <circle cx="250" cy="250" r="202" fill="url(#discGrad)" stroke="rgba(0,168,150,0.2)" stroke-width="2.5"/>

    <!-- Official Authentic Pahilo Paila Footprint Vector/Raster Asset -->
    <image href="data:image/png;base64,{b64}" x="55" y="45" width="390" height="400" preserveAspectRatio="xMidYMid meet" />
  </g>
</svg>'''

with open(r'c:\Users\maste\OneDrive\Desktop\Pahilo Paila\static\img\logo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print('Updated static/img/logo.svg successfully!')
