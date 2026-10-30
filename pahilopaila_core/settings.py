"""
Django settings for Pahilo Paila Montessori project.
Enterprise Grade & Security Hardened with Unfold CMS, PWA, WhiteNoise, and Dynamic Multi-DB.
"""

from pathlib import Path
from decouple import config, Csv
import dj_database_url
from django.templatetags.static import static
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-default-dev-key-change-me')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# Robust host allowance for local dev, ngrok tunnels (*.ngrok-free.dev, *.ngrok-free.app, etc.) and custom domains
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    # Unfold CMS Admin MUST be before django.contrib.admin
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    
    # Third party security and performance tools
    "corsheaders",
    
    # In-house School App
    "school",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "school.middleware.SecurityHeadersMiddleware",
]

ROOT_URLCONF = "pahilopaila_core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "school.context_processors.school_context",
            ],
        },
    },
]

WSGI_APPLICATION = "pahilopaila_core.wsgi.application"
ASGI_APPLICATION = "pahilopaila_core.asgi.application"

# Database: Dynamic according to environment.
DATABASE_URL = config('DATABASE_URL', default='sqlite:///db.sqlite3')

if DATABASE_URL.startswith("sqlite"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            'OPTIONS': {
                'timeout': 20,
            }
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 8}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kathmandu"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security & CORS Settings
CSRF_TRUSTED_ORIGINS = [
    'https://*.ngrok-free.dev',
    'https://*.ngrok-free.app',
    'https://*.ngrok.io',
    'https://*.ngrok.app',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://127.0.0.1',
    'http://localhost',
]
CORS_ALLOW_ALL_ORIGINS = True

# Unfold Theme Customization
UNFOLD = {
    "SITE_TITLE": "Pahilo Paila Montessori CMS",
    "SITE_HEADER": "Pahilo Paila Portal",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("img/logo.svg"),
        "dark": lambda request: static("img/logo.svg"),
    },
    "SITE_LOGO": {
        "light": lambda request: static("img/logo.svg"),
        "dark": lambda request: static("img/logo.svg"),
    },
    "THEME": "dark",
    "COLORS": {
        "primary": {
            "50": "240 253 250",
            "100": "204 251 241",
            "200": "153 246 228",
            "300": "94 234 212",
            "400": "45 212 191",
            "500": "20 184 166",
            "600": "13 148 136",
            "700": "15 118 110",
            "800": "17 94 89",
            "900": "19 78 74",
            "950": "4 47 46",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Navigation & Overview",
                "separator": True,
                "items": [
                    {
                        "title": "Dashboard Overview",
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": "Visit Live Website",
                        "icon": "visibility",
                        "link": "/",
                    },
                ],
            },
            {
                "title": "School Core Management",
                "separator": True,
                "items": [
                    {
                        "title": "Admissions & Inquiries",
                        "icon": "school",
                        "link": reverse_lazy("admin:school_admissioninquiry_changelist"),
                    },
                    {
                        "title": "Programs & Levels",
                        "icon": "menu_book",
                        "link": reverse_lazy("admin:school_program_changelist"),
                    },
                    {
                        "title": "Teachers & Guides",
                        "icon": "groups",
                        "link": reverse_lazy("admin:school_staffmember_changelist"),
                    },
                    {
                        "title": "Activities & Gallery",
                        "icon": "photo_library",
                        "link": reverse_lazy("admin:school_galleryimage_changelist"),
                    },
                    {
                        "title": "Parent Testimonials",
                        "icon": "reviews",
                        "link": reverse_lazy("admin:school_testimonial_changelist"),
                    },
                    {
                        "title": "Contact Messages",
                        "icon": "mail",
                        "link": reverse_lazy("admin:school_contactmessage_changelist"),
                    },
                ],
            },
        ],
    },
}
