from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('programs/', views.programs_view, name='programs'),
    path('programs/<slug:slug>/', views.program_detail_view, name='program_detail'),
    path('admissions/', views.admissions_view, name='admissions'),
    path('admissions/submit/', views.submit_admission_inquiry, name='submit_admission'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('events/', views.events_view, name='events'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/submit/', views.submit_contact_message, name='submit_contact'),
    path('terms/', views.terms_view, name='terms'),
    path('api/push/subscribe/', views.save_push_subscription, name='push_subscribe'),
    path('api/push/test-notification/', views.trigger_instant_notification, name='test_notification'),
    path('sw.js', views.service_worker_js, name='service_worker'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
]
