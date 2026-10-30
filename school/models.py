from django.db import models
from django.utils import timezone

class SchoolInfo(models.Model):
    name = models.CharField(max_length=200, default="Pahilo Paila Montessori School")
    motto = models.CharField(max_length=300, default="Nurturing Curious Minds, Shaping Joyful Futures (पहिलो पाइला)")
    phone = models.CharField(max_length=100, default="984-8636068")
    email = models.EmailField(default="Pahilopaila1@gmail.com")
    address = models.CharField(max_length=300, default="Suda, Mahendranagar, Nepal")
    opening_hours = models.CharField(max_length=100, default="Sun - Fri: 8:30 AM - 4:00 PM")
    about_text = models.TextField(default="Pahilo Paila Montessori School provides authentic, child-centered early childhood education. We nurture curiosity, motor coordination, cognitive growth, and self-directed learning in a loving preschool environment.")
    facebook_url = models.URLField(blank=True, null=True, default="https://www.facebook.com/p/Pahilo-Paila-Montessori-School-61569129280008/")
    instagram_url = models.URLField(blank=True, null=True, default="https://instagram.com")
    youtube_url = models.URLField(blank=True, null=True, default="https://youtube.com")
    
    class Meta:
        verbose_name = "School Configuration"
        verbose_name_plural = "School Configuration"

    def __str__(self):
        return self.name

class Program(models.Model):
    AGE_GROUPS = [
        ('playgroup', 'Playgroup / Toddler (1.5 - 2.5 Years)'),
        ('nursery', 'Nursery (2.5 - 3.5 Years)'),
        ('lkg', 'LKG / Casa Junior (3.5 - 4.5 Years)'),
        ('ukg', 'UKG / Casa Senior (4.5 - 6 Years)'),
        ('afterschool', 'After-School Sensorial Activities (3 - 6 Years)'),
    ]
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    age_group = models.CharField(max_length=50, choices=AGE_GROUPS)
    timing = models.CharField(max_length=100, default="9:30 AM - 2:00 PM")
    capacity = models.PositiveIntegerField(default=15)
    description = models.TextField()
    highlights = models.TextField(help_text="Newline list of key learning highlights")
    icon = models.CharField(max_length=50, default="bi-stars")
    color_accent = models.CharField(max_length=20, default="#FF6B6B")
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.title} ({self.get_age_group_display()})"

    def highlights_list(self):
        return [h.strip() for h in self.highlights.split('\n') if h.strip()]

class StaffMember(models.Model):
    ROLES = [
        ('principal', 'Principal & School Head'),
        ('director', 'Founder & School Director'),
        ('lead_guide', 'Lead Montessori Educator'),
        ('teacher', 'Montessori Teacher'),
        ('care', 'Child Wellness & Caregiver'),
        ('arts', 'Creative Arts & Music Guide'),
    ]
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=50, choices=ROLES)
    qualifications = models.CharField(max_length=250, default="Certified Montessori Early Childhood Educator")
    experience_years = models.PositiveIntegerField(default=5)
    bio = models.TextField()
    avatar_url = models.URLField(blank=True, default="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=600&q=80")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"

class AdmissionInquiry(models.Model):
    STATUS_CHOICES = [
        ('new', 'New Inquiry'),
        ('contacted', 'Contacted / Scheduled Visit'),
        ('visited', 'School Visit Completed'),
        ('enrolled', 'Enrolled'),
        ('archived', 'Archived'),
    ]
    child_name = models.CharField(max_length=150)
    child_dob = models.DateField(verbose_name="Child Date of Birth")
    parent_name = models.CharField(max_length=150)
    parent_email = models.EmailField()
    parent_phone = models.CharField(max_length=50)
    program_interested = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)
    preferred_start_date = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Admission Inquiries"

    def __str__(self):
        return f"Inquiry: {self.child_name} (Parent: {self.parent_name})"

class SchoolEvent(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200, default="Pahilo Paila Montessori, Suda, Mahendranagar")
    description = models.TextField()
    is_public = models.BooleanField(default=True)
    banner_image_url = models.URLField(blank=True, default="https://images.unsplash.com/photo-1588072432836-e10032774350?auto=format&fit=crop&w=1000&q=80")

    class Meta:
        ordering = ['event_date', 'start_time']

    def __str__(self):
        return f"{self.title} - {self.event_date}"

class GalleryImage(models.Model):
    CATEGORIES = [
        ('classroom', 'Classroom Activities & Games'),
        ('sensorial', 'Sensorial & Motor Skills'),
        ('nature', 'Outdoor Play & Fun'),
        ('celebrations', 'Festivals & Birthdays'),
        ('creativity', 'Art, Drawing & Rhymes'),
    ]
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='classroom')
    image_url = models.URLField(help_text="Optimized CDN image URL")
    caption = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    parent_name = models.CharField(max_length=150)
    child_name_and_grade = models.CharField(max_length=150, help_text="e.g. Parent of Aarav (Nursery)")
    rating = models.PositiveIntegerField(default=5)
    content = models.TextField()
    avatar_url = models.URLField(blank=True, default="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=300&q=80")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.parent_name} - {self.child_name_and_grade}"

class Notice(models.Model):
    URGENCY = [
        ('info', 'Information / Update'),
        ('important', 'Important Announcement'),
        ('urgent', 'Urgent / Holiday Notice'),
    ]
    title = models.CharField(max_length=200)
    urgency = models.CharField(max_length=20, choices=URGENCY, default='info')
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return f"[{self.get_urgency_display()}] {self.title}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name}: {self.subject}"

class PushSubscription(models.Model):
    endpoint = models.TextField(unique=True)
    keys_p256dh = models.TextField()
    keys_auth = models.TextField()
    user_agent = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sub #{self.id} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
