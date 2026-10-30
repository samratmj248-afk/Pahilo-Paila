from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    SchoolInfo,
    Program,
    StaffMember,
    AdmissionInquiry,
    SchoolEvent,
    GalleryImage,
    Testimonial,
    Notice,
    ContactMessage,
    PushSubscription
)

@admin.register(SchoolInfo)
class SchoolInfoAdmin(ModelAdmin):
    list_display = ("name", "email", "phone", "opening_hours")

@admin.register(Program)
class ProgramAdmin(ModelAdmin):
    list_display = ("title", "age_group", "timing", "capacity", "is_featured", "order")
    list_filter = ("age_group", "is_featured")
    search_fields = ("title", "description", "highlights")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_featured", "order")

@admin.register(StaffMember)
class StaffMemberAdmin(ModelAdmin):
    list_display = ("name", "role", "qualifications", "experience_years", "order")
    list_filter = ("role",)
    search_fields = ("name", "bio", "qualifications")
    list_editable = ("order",)

@admin.register(AdmissionInquiry)
class AdmissionInquiryAdmin(ModelAdmin):
    list_display = ("child_name", "parent_name", "parent_phone", "program_interested", "status", "created_at")
    list_filter = ("status", "program_interested", "created_at")
    search_fields = ("child_name", "parent_name", "parent_phone", "parent_email")
    list_editable = ("status",)
    readonly_fields = ("created_at", "ip_address")

@admin.register(SchoolEvent)
class SchoolEventAdmin(ModelAdmin):
    list_display = ("title", "event_date", "start_time", "end_time", "location", "is_public")
    list_filter = ("is_public", "event_date")
    search_fields = ("title", "description", "location")
    list_editable = ("is_public",)

@admin.register(GalleryImage)
class GalleryImageAdmin(ModelAdmin):
    list_display = ("title", "category", "order")
    list_filter = ("category",)
    search_fields = ("title", "caption")
    list_editable = ("order",)

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ("parent_name", "child_name_and_grade", "rating", "is_active", "created_at")
    list_filter = ("rating", "is_active")
    search_fields = ("parent_name", "content")
    list_editable = ("is_active",)

@admin.register(Notice)
class NoticeAdmin(ModelAdmin):
    list_display = ("title", "urgency", "publish_date", "expiry_date", "is_active")
    list_filter = ("urgency", "is_active", "publish_date")
    search_fields = ("title", "content")
    list_editable = ("is_active",)

@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_resolved")
    list_filter = ("is_resolved", "created_at")
    search_fields = ("name", "email", "subject", "message")
    list_editable = ("is_resolved",)
    readonly_fields = ("created_at",)

@admin.register(PushSubscription)
class PushSubscriptionAdmin(ModelAdmin):
    list_display = ("id", "user_agent", "created_at")
    readonly_fields = ("endpoint", "keys_p256dh", "keys_auth", "user_agent", "created_at")
