import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages
from django.utils import timezone
from .models import (
    SchoolInfo, Program, StaffMember, AdmissionInquiry,
    SchoolEvent, GalleryImage, Testimonial, Notice, ContactMessage, PushSubscription
)

def home_view(request):
    programs = Program.objects.filter(is_featured=True)[:6]
    staff = StaffMember.objects.all()[:6]
    events = SchoolEvent.objects.filter(is_public=True, event_date__gte=timezone.now().date())[:3]
    gallery_images = GalleryImage.objects.all()[:8]
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    all_programs = Program.objects.all()

    context = {
        'programs': programs,
        'all_programs': all_programs,
        'staff': staff,
        'events': events,
        'gallery_images': gallery_images,
        'testimonials': testimonials,
    }
    return render(request, 'school/index.html', context)

def about_view(request):
    staff = StaffMember.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)
    return render(request, 'school/about.html', {
        'staff': staff,
        'testimonials': testimonials,
    })

def programs_view(request):
    programs = Program.objects.all()
    return render(request, 'school/programs.html', {'programs': programs})

def program_detail_view(request, slug):
    program = get_object_or_404(Program, slug=slug)
    other_programs = Program.objects.exclude(id=program.id)[:3]
    return render(request, 'school/program_detail.html', {
        'program': program,
        'other_programs': other_programs
    })

def admissions_view(request):
    programs = Program.objects.all()
    return render(request, 'school/admissions.html', {'programs': programs})

@csrf_protect
@require_POST
def submit_admission_inquiry(request):
    try:
        child_name = request.POST.get('child_name', '').strip()
        child_dob = request.POST.get('child_dob', '').strip()
        parent_name = request.POST.get('parent_name', '').strip()
        parent_email = request.POST.get('parent_email', '').strip()
        parent_phone = request.POST.get('parent_phone', '').strip()
        program_id = request.POST.get('program_interested', '').strip()
        preferred_start = request.POST.get('preferred_start_date', '').strip() or None
        message = request.POST.get('message', '').strip()

        if not all([child_name, child_dob, parent_name, parent_email, parent_phone]):
            return JsonResponse({'success': False, 'message': 'Please fill in all mandatory fields with valid details.'}, status=400)

        program = Program.objects.filter(id=program_id).first() if program_id else None

        # Capture Client IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        inquiry = AdmissionInquiry.objects.create(
            child_name=child_name,
            child_dob=child_dob,
            parent_name=parent_name,
            parent_email=parent_email,
            parent_phone=parent_phone,
            program_interested=program,
            preferred_start_date=preferred_start,
            message=message,
            ip_address=ip
        )

        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json':
            return JsonResponse({
                'success': True,
                'message': f'Thank you, {parent_name}! Admission inquiry for {child_name} has been received. Our Montessori team will contact you soon.'
            })
        
        messages.success(request, f'Thank you, {parent_name}! Admission inquiry for {child_name} has been received.')
        return redirect('school:admissions')
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Submission failed: {str(e)}'}, status=500)

def gallery_view(request):
    images = GalleryImage.objects.all()
    categories = GalleryImage.CATEGORIES
    return render(request, 'school/gallery.html', {'images': images, 'categories': categories})

def events_view(request):
    upcoming_events = SchoolEvent.objects.filter(is_public=True, event_date__gte=timezone.now().date())
    past_events = SchoolEvent.objects.filter(is_public=True, event_date__lt=timezone.now().date()).order_by('-event_date')[:6]
    return render(request, 'school/events.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    })

def contact_view(request):
    return render(request, 'school/contact.html')

def terms_view(request):
    return render(request, 'school/terms.html')

@csrf_protect
@require_POST
def submit_contact_message(request):
    try:
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not all([name, email, subject, message_text]):
            return JsonResponse({'success': False, 'message': 'Please complete all required fields.'}, status=400)

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message_text
        )

        return JsonResponse({
            'success': True,
            'message': f'Thank you {name}! Your message has been sent to Pahilo Paila Montessori School.'
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error sending message: {str(e)}'}, status=500)

@csrf_exempt
@require_POST
def save_push_subscription(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        endpoint = data.get('endpoint')
        keys = data.get('keys', {})
        p256dh = keys.get('p256dh', '')
        auth = keys.get('auth', '')
        user_agent = request.META.get('HTTP_USER_AGENT', '')[:290]

        if not endpoint or not p256dh or not auth:
            return JsonResponse({'status': 'error', 'message': 'Invalid subscription payload'}, status=400)

        PushSubscription.objects.update_or_create(
            endpoint=endpoint,
            defaults={
                'keys_p256dh': p256dh,
                'keys_auth': auth,
                'user_agent': user_agent
            }
        )
        return JsonResponse({'status': 'success', 'message': 'Push subscription registered successfully.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def trigger_instant_notification(request):
    return JsonResponse({
        'title': '🎉 Pahilo Paila Montessori School',
        'body': 'Admissions Open! Explore our Montessori learning activities in Suda, Mahendranagar.',
        'icon': '/static/img/icon-192.png',
        'badge': '/static/img/icon-192.png',
        'url': '/admissions/'
    })

def service_worker_js(request):
    sw_code = """
const CACHE_NAME = 'pahilo-paila-v1.0.1';
const STATIC_ASSETS = [
  '/',
  '/about/',
  '/programs/',
  '/admissions/',
  '/gallery/',
  '/events/',
  '/contact/',
  '/static/css/style.css',
  '/static/js/main.js',
  '/static/manifest.json',
  '/static/img/icon-192.png',
  '/static/img/icon-512.png',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css',
  'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css',
  'https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(STATIC_ASSETS).catch(err => console.warn('Cache addAll non-fatal error:', err));
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  
  event.respondWith(
    caches.match(event.request).then(cachedResponse => {
      const fetchPromise = fetch(event.request).then(networkResponse => {
        if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      }).catch(() => {
        return cachedResponse;
      });
      return cachedResponse || fetchPromise;
    })
  );
});

self.addEventListener('push', event => {
  let data = {
    title: 'Pahilo Paila Montessori',
    body: 'New update from our Montessori learning community!',
    icon: '/static/img/icon-192.png',
    badge: '/static/img/icon-192.png',
    url: '/'
  };
  
  if (event.data) {
    try {
      data = Object.assign(data, event.data.json());
    } catch(e) {
      data.body = event.data.text();
    }
  }

  event.waitUntil(
    self.registration.showNotification(data.title, {
      body: data.body,
      icon: data.icon,
      badge: data.badge,
      data: { url: data.url },
      vibrate: [200, 100, 200]
    })
  );
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  const targetUrl = event.notification.data?.url || '/';
  event.waitUntil(
    clients.matchAll({ type: 'window' }).then(clientList => {
      for (const client of clientList) {
        if (client.url === targetUrl && 'focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow(targetUrl);
      }
    })
  );
});
"""
    return HttpResponse(sw_code, content_type="application/javascript")

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
        "Sitemap: " + request.build_absolute_uri('/sitemap.xml'),
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def sitemap_xml(request):
    base_url = request.build_absolute_uri('/')[:-1]
    pages = [
        {'loc': f"{base_url}/", 'changefreq': 'daily', 'priority': '1.0'},
        {'loc': f"{base_url}/about/", 'changefreq': 'weekly', 'priority': '0.8'},
        {'loc': f"{base_url}/programs/", 'changefreq': 'weekly', 'priority': '0.9'},
        {'loc': f"{base_url}/admissions/", 'changefreq': 'daily', 'priority': '0.95'},
        {'loc': f"{base_url}/gallery/", 'changefreq': 'weekly', 'priority': '0.7'},
        {'loc': f"{base_url}/events/", 'changefreq': 'daily', 'priority': '0.85'},
        {'loc': f"{base_url}/contact/", 'changefreq': 'monthly', 'priority': '0.8'},
    ]
    
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in pages:
        xml.append(f"  <url><loc>{p['loc']}</loc><changefreq>{p['changefreq']}</changefreq><priority>{p['priority']}</priority></url>")
    
    for prog in Program.objects.all():
        xml.append(f"  <url><loc>{base_url}/programs/{prog.slug}/</loc><changefreq>weekly</changefreq><priority>0.85</priority></url>")

    xml.append('</urlset>')
    return HttpResponse("\n".join(xml), content_type="application/xml")
